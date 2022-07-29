from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='main' ),
    path('students/', views.students, name='students' ),
    path('exams/', views.exams, name='exams' ),
    path('cbc/', views.cbc, name='cbc' ),
    path('timetable/', views.timetable, name='timetable' ),
]
