from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.conf import settings

from os import listdir
from os.path import isfile, join

from .models import Person, History, Datacenter, Institution, Service, SubService, Paper, Thesis

class IndexView(generic.ListView):
	template_name = 'main/index.html'

	def get_queryset(self):
		pass

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['services'] = Service.objects.all().order_by('index')
		return context

class HistoryView(generic.ListView):
	template_name = 'main/history.html'
	context_object_name = 'histories'

	def get_queryset(self):
		return History.objects.all()

	def get_context_data(self, **kwargs):
		context = super(HistoryView, self).get_context_data(**kwargs)
		context['services'] = Service.objects.all().order_by('index')
		return context

class ServicesView(generic.ListView):
	template_name = 'main/services.html'
	context_object_name = 'services'

	def get_queryset(self):
		services = Service.objects.all().order_by('index')
		for serv in services:
			serv.subservices = SubService.objects.filter(service=serv.id).order_by('index')
		return services

class DatacenterView(generic.ListView):
	template_name = 'main/datacenter.html'
	context_object_name = 'datacenters'

	def get_queryset(self):
		return Datacenter.objects.all()

	def get_context_data(self, **kwargs):
		context = super(DatacenterView, self).get_context_data(**kwargs)

		mypath = join(settings.MEDIA_ROOT,'datacenter')
		gallery = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		gallery.sort()

		context['gallery'] = gallery
		context['services'] = Service.objects.all().order_by('index')
		# And so on for 
		return context

class StaffView(generic.ListView):
	template_name = 'main/staff.html'
	context_object_name = 'staff'

	def get_queryset(self):
		return Person.objects.all()

	def get_context_data(self, **kwargs):
		context = super(StaffView, self).get_context_data(**kwargs)
		# Get the institutions:
		context['institutions'] = Institution.objects.all()
		# Get last fives:
		context['lastnews'] = Person.objects.all()[:5]
		context['services'] = Service.objects.all().order_by('index')
		return context

class DocumentsView(generic.ListView):
	template_name = 'main/documents.html'

	def get_queryset(self):
		pass

	def get_context_data(self, **kwargs):
		context = super(DocumentsView, self).get_context_data(**kwargs)
		context['services'] = Service.objects.all().order_by('index')

		l = []
		papers = Paper.objects.all().order_by('-date')
		for paper in papers:
			paper.type = 'paper'
			l.append(paper)
		thesis = Thesis.objects.all().order_by('-date')
		for thes in thesis:
			thes.type = 'thesis'
			l.append(thes)
		l.sort(key=lambda x: x.date, reverse=True)
		context['docs'] = l
		context['papers'] = papers
		context['thesis'] = thesis

		return context