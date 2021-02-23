from django.shortcuts import render
from courses.models import Course
from django.shortcuts import get_object_or_404
from .forms import CoursesForms

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'cursos/cursos.html', context)


'''def details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course
    }
    return render(request, 'cursos/details.html', context)'''


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course,
        'forms': CoursesForms
    }
    return render(request, 'cursos/details.html', context)
