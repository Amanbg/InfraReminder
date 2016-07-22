from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from django.core import validators
from datetime import date

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

	class Meta:
		db_table = 'reminder_table'
		verbose_name = 'reminder_table'
		verbose_name_plural = 'reminder_tables'

	def __unicode__(self):
		return self.email_id