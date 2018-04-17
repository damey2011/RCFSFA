# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 07:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20171004_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatorprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coord_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='excoprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exco_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='member_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
