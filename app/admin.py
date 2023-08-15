from django.contrib import admin
from .models import *

# Register your models here.
for model in (Student, Course, Score):
    admin.site.register(model)
