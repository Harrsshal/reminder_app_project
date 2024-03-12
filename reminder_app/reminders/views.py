from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.http import HttpResponse
from .models import Reminder
from .serializers import ReminderSerializer
# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Reminder App!")

@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
