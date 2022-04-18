from django.urls import path
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('lists/', views.attendancesList, name='list'),
    path('<int:pk>/delete/', views.attendanceDelete, name='delete'),
]