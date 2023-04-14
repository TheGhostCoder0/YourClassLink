from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseForm
from django.urls import reverse
from utils import notification


# Create your views here.
def add_course(request):
    show_modal = False  # set the initial value of show_modal to False

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()  # clear the form
            show_modal = True  # set show_modal to True when the form is successfully submitted
            notification()

    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form, 'show_modal': show_modal})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})


