from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseForm
from django.urls import reverse


# Create your views here.
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()  # clear the form
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})


def request_university(request):
    if request.method == 'POST':
        # Handle the form submission
        # Extract form data from request.POST dictionary
        name = request.POST.get('name')
        # Do any additional processing of form data as needed
        # ...
        # Return a success message
        return render(request, 'university_list.html')
    else:
        # Render the university request form
        return render(request, 'university_list.html')
