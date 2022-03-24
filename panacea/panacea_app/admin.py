from django.contrib import admin

# Register your models here.
from .models import *

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("doc_id", "name", "email", "licence_no")

admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("pat_id", "name", "email")

admin.site.register(Patient, PatientAdmin)