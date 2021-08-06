from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class BlogView(TemplateView):
    template_name = "blog.html"

class BookView(TemplateView):
    template_name = "bookings.html"

class ClassView(TemplateView):
    template_name = "classes.html"
