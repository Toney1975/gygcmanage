from django.contrib import admin
from .models import Instrument,Instrumentfaults
# Register your models here.
admin.site.register(Instrumentfaults)
admin.site.register(Instrument)