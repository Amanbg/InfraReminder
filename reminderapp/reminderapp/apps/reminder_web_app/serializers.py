from rest_framework import serializers
from reminder_web_app.models import Reminder 

class ReminderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reminder
		fields = ('url','date','time','email_id','phone_no','message')