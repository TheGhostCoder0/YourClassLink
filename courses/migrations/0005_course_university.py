# Generated by Django 4.1.7 on 2023-04-03 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_data_created_course_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.university'),
        ),
    ]
