from django.contrib import admin
from .models import Task
# Register your models here.



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'assigned_to', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'due_date', 'assigned_to')
