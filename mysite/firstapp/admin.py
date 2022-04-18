from django.contrib import admin

# Register your models here.

from .models import sensorData
 
@admin.register(sensorData)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
sensorData._meta.get_fields()]
