# Generated by Django 4.2.7 on 2024-01-28 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_appointment_category_subscribers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]