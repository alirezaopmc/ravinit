# Generated by Django 4.2.4 on 2023-08-12 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_course_students_alter_score_course_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('student', 'course')},
        ),
    ]
