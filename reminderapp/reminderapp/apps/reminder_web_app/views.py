from django.shortcuts import render
from reminder_web_app.models import Reminder
from reminder_web_app.serializers import ReminderSerializer
from rest_framework import viewsets

# Create your views here.
class ReminderViewSet(viewsets.ModelViewSet):
	queryset = Reminder.objects.all()
	serializer_class = ReminderSerializer
