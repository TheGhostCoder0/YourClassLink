from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import University, Course, Quarter
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import notify_new_university
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def university_list(request):
    universities = University.objects.all()
    return render(request, 'university/university_list.html', {'universities': universities})


def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    quarters = Quarter.objects.filter(course__university=university).distinct()

    quarter_course_map = {}
    for quarter in quarters:
        courses = Course.objects.filter(university=university, quarter=quarter)
        quarter_course_map[quarter] = courses

    context = {
        'university': university,
        'quarter_course_map': quarter_course_map,
    }
    return render(request, 'university/university_detail.html', context)


def about(request):
    return render(request, 'about/about.html')


def search(request):
    query = request.GET.get('q')
    if query:
        words = query.split()
        courses = Course.objects.all()
        matches = []
        for course in courses:
            words_list = course.course_name.split() + course.course_ID.split() + \
                         course.university.name.split() + \
                         [course.quarter.quarter, str(course.quarter.year)]
            for word in words:
                if word.lower() in [w.lower() for w in words_list]:
                    matches.append(course)
                    break
        if len(matches) == 0:
            return render(request, 'no_results.html', {'query': query})
        elif len(matches) == 1:
            return render(request, 'multiple_results.html', {'matches': matches})
        else:
            return render(request, 'multiple_results.html', {'matches': matches})
    else:
        return redirect('/')


def request_university(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        notify_new_university(name)
        return render(request, 'university/request_university.html', {'show_modal': True})
    return render(request, 'university/request_university.html')


def sitemap(request):
    with open('sitemap.xml', 'r') as f:
        response = HttpResponse(f.read(), content_type='application/xml')
    return response


def custom_404(request, exception):
    return render(request, '404.html', status=404)




