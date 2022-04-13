# Generated by Django 3.2.7 on 2022-04-13 14:38

import django.core.validators
from django.db import migrations, models
import geonode.people.utils


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0036_merge_20210706_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator(), geonode.people.utils.unique_email_validator], verbose_name='email address'),
        ),
    ]
