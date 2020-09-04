from django.shortcuts import render, get_object_or_404
from .models import Day

def day_list (request):
    days = Day.Public.all()
    return render (request,
                'diary/day/list.html',
                {'days': days})

def day_detail (request, year, month, date_day, day):
    day = get_object_or_404 (Day, Slug = day,
                            Privacy = 'public',
                            Last_Edit_Time__year = year,
                            Last_Edit_Time__month = month,
                            Last_Edit_Time__day = date_day)
    return render(request,
                'diary/day/detail.html',
                 {'day' : day})
