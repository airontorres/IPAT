# Generated by Django 4.2.13 on 2024-07-06 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_agency_em_item_blood_type_item_citizenship_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date_created',
        ),
    ]
