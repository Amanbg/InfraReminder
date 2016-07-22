# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 08:15
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('email_id', models.EmailField(blank=True, help_text='Valid Email Address', max_length=254, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Enter a valid email address')], verbose_name='Email Address')),
                ('phone_no', models.CharField(blank=True, help_text='A valid Phone No.', max_length=10, null=True, validators=[django.core.validators.RegexValidator('^([7|8|9]\\d{9})$', 'Enter a valid Phone Number')], verbose_name='Phone no.')),
                ('message', models.CharField(max_length=50, verbose_name='Reminder Message')),
            ],
            options={
                'db_table': 'reminder_table',
                'verbose_name': 'reminder_table',
                'verbose_name_plural': 'reminder_tables',
            },
        ),
    ]
