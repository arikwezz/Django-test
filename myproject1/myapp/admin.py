from django.contrib import admin
from .models import Resume 
@admin.register(Resume) 
class TaskAdmin(admin.ModelAdmin): 
    list_display = ('fullname', 'email')  # Поля, которые будут отображаться в списке
    search_fields = ('full_name',)  # Поиск по названию задачи 
    list_filter = ('data_field',)  # Фильтр по дате создания