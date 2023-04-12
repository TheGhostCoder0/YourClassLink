from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_course, name='add_course'),
    path('<int:course_id>', views.detail, name='detail'),
]
