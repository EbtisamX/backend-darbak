from django.contrib import admin

# Register your models here.
from .models import JobApplication,Note
admin.site.register(JobApplication)
admin.site.register(Note)
