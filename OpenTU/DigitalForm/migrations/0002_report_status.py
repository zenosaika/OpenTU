# Generated by Django 4.2.10 on 2024-02-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]