from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Module, Professor

def all_courses(request):
	all_courses = Course.objects.all()
	return render(request, 'courses/all_courses.html', {'all_courses': all_courses})

def all_professors(request):
	all_professors = Professor.objects.all()
	return render(request, 'courses/all_professors.html', {'all_professors': all_professors})

def all_modules(request):
	all_modules = Module.objects.all()
	return render(request, 'courses/all_modules.html', {'all_modules': all_modules})

def professor_courses(request, professor_name):
	professor_courses = Course.objects.filter(professor__name=professor_name)
	return render(request, 'courses/professor_courses.html', {'professor_name': professor_name, 'professor_courses': professor_courses})

def module_courses(request, module_name):
	module_courses = Course.objects.filter(module__name=module_name)
	return render(request, 'courses/module_courses.html', {'module_name': module_name, 'module_courses': module_courses})

def search(request):
	return render(request, 'courses/search.html', {})



