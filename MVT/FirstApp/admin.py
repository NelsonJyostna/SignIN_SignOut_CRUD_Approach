from django.contrib import admin
from .models import  Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['rn', 'name', 'marks', 'city','Dist']
admin.site.register(Student, StudentAdmin)