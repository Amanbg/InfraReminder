from celery import Task
from reminder_web_app.models import Reminder
from datetime import datetime, timedelta
from config.celery import app
from django.core.exceptions import ValidationError
from datetime import datetime
import time

@app.task
def createReminder():
    """
    Create Reminder on the basis of user input date and time.It first get the corresponding date 
    and time from the user then find the time delta by comparing the current time which is in IST(Indian Time) 
    and given time (IST).
    Get the difference between two timestamps called timeDelta .Since celery work in UTC time so add 
    this timedelta to the UTC current time to get the future UTC time for the reminder. Once the Reminder 
    future time (UTC) matches with the UTC current time ,it will display reminder ring up and also set the 
    reminder_received field in the Reminder model to TRUE which is initially FALSE.
    I have add this field to the model to keep a check whether reminder occurs or not.
    """
    try:
        reminder_object = None
        while reminder_object is None:
            try:
                reminder_object = Reminder.objects.get(reminder_received=False)
            except Exception as e:
                print str(e)
                return False

            s1 = str(reminder_object.date)+" "+str(reminder_object.time) #User input IST date time
        
            s2 = datetime.now() # current IST time 
            s2 = s2.strftime("%Y-%m-%d %H:%M:%S")
        
            FMT = "%Y-%m-%d %H:%M:%S"
            tdelta = datetime.strptime(s1,FMT) - datetime.strptime(s2,FMT)  # time delta      
            result_utc = datetime.utcnow() + timedelta(seconds=tdelta.seconds)  #add this time delta to get Future UTC time.
            
            result_utc = result_utc.replace(microsecond=0) #set microsecond to 0 as user does not input microseconds.
            
            current_utc = datetime.utcnow().replace(microsecond=0) #similarly here
            
            if current_utc < result_utc:
                pass
            elif current_utc==result_utc:
                print"Reminder Ring Up.. "
                reminder_object.reminder_received=True
                reminder_object.save()
            return True
    except Exception as e:
        print str(e)

