"""yourClassLink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.courses, name='courses')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='courses')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import CourseResource
from . import views

course_resource = CourseResource()

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('api/', include(course_resource.urls)),
    path('university/', views.university_list, name='university'),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('contact/', include('contact.urls'), name='contact'),
    path('university/request', views.request_university, name='request_university')

]
