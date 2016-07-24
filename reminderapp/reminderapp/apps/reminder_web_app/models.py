from __future__ import unicode_literals
from django.db import models
from reminderapp.config import celery_app
from django.utils.translation import ugettext as _
from django.core import validators
from datetime import datetime
from datetime import date
from datetime import timedelta
# Create your models here.

class Reminder(models.Model):
    date = models.DateField(_("Date"), default=date.today)
    time = models.TimeField(_("Time"))
    email_id = models.EmailField(
                _("Email Address"),
                blank=True,
                null=True,
                help_text=('Valid Email Address'),
                validators=[
                            validators.RegexValidator(
                            r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',
                            _('Enter a valid email address')
                            ),
                ],
    )
    phone_no = models.CharField(
                _("Phone no."),
                max_length=10,
                blank=True, 
                null=True,
                help_text=('A valid Phone No.'),
                validators=[
                            validators.RegexValidator(
                            r'^([7|8|9]\d{9})$',
                            _('Enter a valid Phone Number')
                            ),
                ],
    )
    message = models.CharField(_("Reminder Message"), max_length=50)
    reminder_received = models.BooleanField(default=False)

    class Meta:
        db_table = 'reminder_table'
        verbose_name = 'reminder_table'
        verbose_name_plural = 'reminder_tables'

    def __unicode__(self):
        return self.email_id

    def schedule_reminder(self):
        """Schedules a Celery task to send a reminder"""
        # Calculate the correct time to send this reminder

        # s1 = str(self.date)+" "+str(self.time)
        # print "s1 : ",s1
        # s2 = datetime.now()
        # s2 = s2.strftime("%Y-%m-%d %H:%M:%S")
        # print "s2 : ",s2
        # FMT = "%Y-%m-%d %H:%M:%S"
        # tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)
        # print "tdelta : ", tdelta
        # # reminder_time = appointment_time.replace(minutes=-settings.REMINDER_TIME)
        # result_utc = datetime.utcnow() + timedelta(seconds=tdelta.seconds,microseconds=tdelta.microseconds)
        # # Schedule the Celery task
        # print "result_utc : ",result_utc
        from .tasks import createReminder
        # result = createReminder.apply_async((self.pk,), eta=result_utc)
        createReminder(self.pk)
        # return result.id