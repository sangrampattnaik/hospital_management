from django.contrib import admin

from . import models


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id','patient_name']


@admin.register(models.EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['event_name','category']

@admin.register(models.PhysicianSpeciality)
class PhysicianSpecialityAdmin(admin.ModelAdmin):
    list_display = ['id','speciality_name']

@admin.register(models.PatientTreatment)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id','event_name','physician_id']


