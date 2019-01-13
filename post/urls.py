from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('new', views.new, name='new'),
    path('<int:idea_id>/', views.detail, name='detail'),
    path('<int:year>/<int:month>/<int:day>', views.detail_date, name='detail_date'),
    path('<int:idea_id>/edit', views.edit, name='edit'),
    path('calendar/<int:year>/<int:month>', views.calendar, name='calendar'),
    path('calendar', views.calendar_today, name='calendar_today'),
    path('list', views.list, name='list'),
]
