from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ward)
class wardAdmin(admin.ModelAdmin):
    list_display = ('ward_id', 'ward_name', 'number_beds', 'nurse_in_charge', 'ward_type')
    ordering = ('ward_id',)
@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'initials', 'sex', 'address', 'post_code', 'admission', 'DOB', 'ward_id', 'next_of_kin')
    ordering = ('patient_id',)