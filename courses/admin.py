from django.contrib import admin
from .models import University, Quarter, Course


# Register your models here.
class QuarterAdmin(admin.ModelAdmin):
    list_display = ('id', 'quarter', 'year')


class CourseAdmin(admin.ModelAdmin):
    exclude = ('date_created', )


admin.site.register(University)
admin.site.register(Quarter, QuarterAdmin)
admin.site.register(Course, CourseAdmin)
