# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.views.generic import ListView, DetailView

from .models import Course, Lesson


class CourseListView(ListView):
	model = Course

class CourseDetailView(DetailView):
	model = Course