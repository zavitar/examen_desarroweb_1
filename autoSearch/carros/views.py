# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView

from  .models import Car

# Create your views here.
def lago(request):
	return render(request,"home.html")



class car_list(ListView):
	template_name='car_list.html'
	queryset=Car.objects.all()

class car_datail(DetailView):
	template_name='car_datail.html'
	queryset= Car.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		print id
		return Car.objects.get(id=id)

	
	