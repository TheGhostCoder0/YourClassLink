from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quarter(models.Model):
    quarter = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        title = f"{self.quarter}{self.year}"
        return title


class Course(models.Model):
    course_ID = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        title = f"{self.course_ID}: {self.course_name}"
        return title


class CourseForm(forms.ModelForm):
    university = forms.ModelChoiceField(queryset=University.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = Course
        fields = ['course_ID', 'course_name', 'quarter', 'university', 'link']
        widgets = {
            'course_ID': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'quarter': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'link': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].label = 'Quarter/Semester'


