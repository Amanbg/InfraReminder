from celery import Task
from reminder_web_app import models
# from reminder_web_app.models import Reminder
from datetime import datetime, timedelta
from config.celery import app
from django.core.exceptions import ValidationError
from datetime import datetime
import time

count = 1

@app.task
def createReminder(count):
    try:
        reminder_object = None
        while reminder_object is None:
            try:
                reminder_object = Reminder.object.get(id=count)
            except:
                count = count +1

        offset = datetime.utcnow() - datetime.now()

        remind_time = reminder_object.date + " " + reminder_object.time
        print "remind_time :",remind_time
        
        localtime = datetime.strptime(remind_time,"%Y-%m-%d %H:%M:%S")
        
        result_utc = localtime+offset

        if result_utc==datetime.utcnow():
            print"Reminder Ring Up.. "
            reminder_object.reminder_received=True
            reminder_object.save()

        createReminder(count).apply_async(eta=result_utc)
        return True
    except Exception as e:
        print str(e)


