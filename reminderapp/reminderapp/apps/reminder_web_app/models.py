from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _

from datetime import date
# Create your models here.
class Reminder(models.Model):
	date = models.DateField(_("Date"), default=date.today)
	time = models.TimeField(_("Time"))
	email_id = models.EmailField(_("Email Address"),blank=True, null=True)
	phone_no = models.CharField(_("Phone no."),max_length=10, blank=True, null=True)
	message = models.CharField(_("Reminder Message"), max_length=50)

	class Meta:
		db_table = 'reminder_table'
		verbose_name = 'reminder_table'
		verbose_name_plural = 'reminder_tables'

	def __unicode__(self):
		return '%s' % self.email_id