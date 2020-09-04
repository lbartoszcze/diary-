from django.urls import path
from . import views
app_name = 'diary'
urlpatterns = [
    path('', views.day_list, name = 'day_list'),
    path('<int:year>/<int:month>/<int:date_day>/<slug:day>',
        views.day_detail,
        name = 'day_detail'),
]
