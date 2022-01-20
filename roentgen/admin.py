from django.contrib import admin

from .models import PatientModel, PatientRecordsModel


admin.site.register(PatientModel)
admin.site.register(PatientRecordsModel)
