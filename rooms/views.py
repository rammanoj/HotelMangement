from django.db.models import Q
from django.shortcuts import get_object_or_404
import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView


# Block Views

class BlockListCreateView(ListCreateAPIView):
    serializer_class = serializers.BlockSerializer

    def get_queryset(self):
        if self.request.user.groups.all()[0].name == 'Admin':
            return models.Block.objects.all()
        else:
            return models.Block.objects.none()

    def post(self, request, *args, **kwargs):
        if self.request.user.groups.all()[0].name != 'Admin':
            return Response({'message': 'Permission denied', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(BlockListCreateView, self).post(request, *args, **kwargs)


class BlockRetrieveUpdateDesroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BlockSerializer

    def get_queryset(self):
        if self.request.user.groups.all()[0].name == 'Admin':
            return models.Block.objects.all()
        else:
            return models.Block.objects.none()

# End of Block Views.


# Room Views

class RoomListView(ListAPIView):
    serializer_class = serializers.RoomListSerializer
    queryset = models.Room.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.groups.all()[0].name != 'Admin':
            return Response({'message': 'Permission denied', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        context = super(RoomListView, self).get(request, *args, **kwargs)
        booked_rooms = models.Room.objects.filter(booking__status=1)
        for i in context.data['results']:
            i['booked'] = booked_rooms.filter(room_no=i['room_no']).exists()
        return context

    def post(self, request, *args, **kwargs):
        rooms = models.Room.objects.all()
        try:
            start_date = request.data['start_date']
            end_date = request.data['end_date']
            booked_rooms = models.Room.objects.filter(Q(booking__status=0), Q(booking__status=1))
            free_rooms = booked_rooms.filter(Q(Q(booking__check_in__gt=start_date), Q(booking__check_in__gt=end_date))
                                                | Q(booking__check_in__lt=end_date), Q(booking__check_out__lt=start_date))
            booked_rooms = booked_rooms.exclude(free_rooms)
            rooms = rooms.exclude(booked_rooms)
        except KeyError:
            return Response({'message': 'Fill the form completely!!', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        self.queryset = rooms
        return super(RoomListView, self).post(request, *args, **kwargs)


class RoomCreateSerializer(CreateAPIView):
    serializer_class = serializers.RoomSerializer

    def post(self, request, *args, **kwargs):
        if request.user.groups.all()[0].name != 'Admin':
            return Response({'message': 'Permission denied', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        super(RoomCreateSerializer, self).post(request, *args, **kwargs)
        return Response({'message': 'Successfully created room', 'error': 0}, status=status.HTTP_200_OK)


class RoomRetrieveUpdateDeleteSerializer(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoomSerializer

    def update(self, request, *args, **kwargs):
        if request.user.groups.all()[0].name != 'Admin':
            return Response({'message': 'Permission denied', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        return super(RoomRetrieveUpdateDeleteSerializer, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if request.user.groups.all()[0].name != 'Admin':
            return Response({'message': 'Permission denied', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        super(RoomRetrieveUpdateDeleteSerializer, self).post(request, *args, **kwargs)
        return Response({'message': 'Successfully Deleted!', 'error': 1}, status=status.HTTP_200_OK)

# End of Room Views


# Bookings views.

class RoomBookingListCreateView(ListCreateAPIView):
    serializer_class = serializers.RoomBookingSerializer

    def get_queryset(self):
        if self.request.user.groups.all()[0].name == 'Admin':
            return models.BookedUsers.objects.order_by('booked_date')
        else:
            return models.BookedUsers.objects.filter(Q(user=self.request.user)).order_by('booked_date')

    def post(self, request, *args, **kwargs):
        # Check if the Admin entered the username while making a offline booking.
        request.data['user'] = request.user
        if request.user.groups.all()[0].name == 'Admin':
            try:
                username = request.data['username']
            except KeyError:
                return Response({'message': 'Enter the username of the offline booking user.'})

        # Validate the serialised data, raise Exception if any
        s = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response({'message': 'Successfully created Room', 'error': 1})


class RoomBookingRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookedUsers

    def get_object(self):
        obj = get_object_or_404(models.BookedUsers, pk=self.kwargs['pk'])
        if obj.user.groups.all()[0].name == 'Admin':
            return obj
        elif obj.user == self.request.user:
            return obj
        else:
            return get_object_or_404(models.BookedUsers, pk=-1)

    def update(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        room_no = [models.Room.objects.get(i) for i in request.data['room_no']]
        room_booking = models.Booking.objects.filter(booked_by=obj)
        for i in room_booking:
            # Can delete some specifc rooms in the entire room booking.
            booked_room = i
            if booked_room.room in room_no:
                booked_room['status'] = -1
                booked_room.save()

        return Response({'message': 'Cancelled Booking', 'error': 0})

# End of Room Booking views


# Report check-in or check-out

class RoomReportView(APIView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            reference = request.data['reference']
            room = request.data['room']
            room_status = request.data['status']
        except KeyError:
            return Response({'message': 'Something went wrong, Try again later', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)

        booking = models.Booking.objects.filter(Q(reference=reference), Q(room=room))
        if booking.exists():
            booking.status = room_status
            booking.save()
        else:
            return Response({'message': 'No such booking is performed!!', 'error': 1}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Successfully done', 'error': 0})

# End of Report check-in or check-out
