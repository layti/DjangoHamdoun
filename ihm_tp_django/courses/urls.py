from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_courses, name="all_courses"),
    url(r'^professors/$', views.all_professors, name="all_professors"),
    url(r'^modules/$', views.all_modules, name="all_modules"),
    url(r'^professor/(?P<professor_name>\w+)$', views.professor_courses, name="professor_courses"),
    url(r'^module/(?P<module_name>\w+)$', views.module_courses, name="module_courses"),
    url(r'^search/$', views.search, name="search"),
]
