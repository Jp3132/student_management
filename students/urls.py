# students/urls.py






from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/edit/<int:pk>/', views.student_edit, name='student_edit')
]