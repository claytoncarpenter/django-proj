from django.contrib import admin

# Register your models here.

from .models import sensorData, lightData, myTodo
 
@admin.register(sensorData)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
sensorData._meta.get_fields()]

@admin.register(lightData)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
lightData._meta.get_fields()]

@admin.register(myTodo)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
myTodo._meta.get_fields()]

