# Generated by Django 4.2.10 on 2024-02-20 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dorm', '0005_bill_payment_status'),
        ('User', '0008_remove_student_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Dorm.room'),
            preserve_default=False,
        ),
    ]
