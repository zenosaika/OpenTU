# Generated by Django 4.2.10 on 2024-02-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_course_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='final_duration_hr',
            field=models.FloatField(default=3.0),
        ),
        migrations.AddField(
            model_name='course',
            name='final_exam_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='midterm_duration_hr',
            field=models.FloatField(default=2.0),
        ),
        migrations.AddField(
            model_name='course',
            name='midterm_exam_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
