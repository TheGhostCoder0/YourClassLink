from django.db import models
from tastypie.resources import ModelResource
from courses.models import Course


# Create your models here.
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        excludes = ['date_created']
