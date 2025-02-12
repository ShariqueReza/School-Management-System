# Generated by Django 5.1.4 on 2025-01-17 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_all_students_student_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
        migrations.AddField(
            model_name='all_students',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.all_students'),
        ),
    ]
