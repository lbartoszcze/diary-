from django.contrib import admin
from .models import Day
@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('Profile', 'Date','Name', 'Happiness_Score', 'Description', 'Slug', 'Last_Edit_Time')
    list_filter = ('Date', 'Happiness_Score')
    search_fields = ['Description', 'Name']
    raw_id_fields = ('Profile',)
    date_hierarchy = 'Date'
    prepopulated_fields = {'Slug': ('Name',)}
