# Generated by Django 4.2.10 on 2024-02-21 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalForm', '0002_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
