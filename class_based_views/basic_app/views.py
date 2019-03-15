from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailsView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'

class CreateSchoolView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class UpdateSchoolView(UpdateView):
    fields = ('principal',)
    model = models.School

class DeleteSchoolView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
