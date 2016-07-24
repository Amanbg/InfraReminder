from celery import Task
from reminder_web_app.models import Reminder
from datetime import datetime, timedelta
from config.celery import app
from django.core.exceptions import ValidationError
from datetime import datetime
import time

count =1

@app.task
def createReminder(reminder_id):
    
    try:
        reminder_object = None
        while reminder_object is None:
            try:
                reminder_object = Reminder.objects.get(id=reminder_id)
            except:
                pass

        s1 = str(reminder_object.date)+" "+str(reminder_object.time)
        # print "s1 : ",s1
        s2 = datetime.now()
        s2 = s2.strftime("%Y-%m-%d %H:%M:%S")
        # print "s2 : ",s2
        FMT = "%Y-%m-%d %H:%M:%S"
        tdelta = datetime.strptime(s1,FMT) - datetime.strptime(s2,FMT)
        # if tdelta.days < 0:
        #     print "tdelta < 0",tdelta.days
        #     tdelta = timedelta(days=0,
        #         seconds=tdelta.seconds)

        # print "tdelta : ", tdelta
        result_utc = datetime.utcnow() + timedelta(seconds=tdelta.seconds)
        
        result_utc = result_utc.replace(microsecond=0)
        # print "result_utc : ",result_utc

        current_utc = datetime.utcnow().replace(microsecond=0)
        
        # print "current utc : ",current_utc
        if current_utc < result_utc:
            pass
        elif current_utc==result_utc:
            print"Reminder Ring Up.. "
            reminder_object.reminder_received=True
            reminder_object.save()

        createReminder.apply_async((reminder_id,),eta=result_utc)
        return True
    except Exception as e:
        print str(e)


