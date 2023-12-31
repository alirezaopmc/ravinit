# Generated by Django 4.2.4 on 2023-08-12 06:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('courses', models.ManyToManyField(related_name='courses', to='app.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='students', to='app.student'),
        ),
    ]
