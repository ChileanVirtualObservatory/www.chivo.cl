import time

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from hitcount.views import HitCountDetailView
from hitcount.models import HitCount

from main.models import Service
from .models import Article

class PopNews:
	plist = []
	limit = 5
	last_change = 0

	def get(self, obj_list):
		t_now  = time.time()
		t_diff = t_now - self.last_change

		if t_diff > 3600:
			self.last_change = t_now
			self.plist[:] = []

			for article in obj_list:
				hit_count = HitCount.objects.get_for_object(article)
				article.hits = hit_count.hits
				self.plist.append(article)

			self.plist.sort(key=lambda x: x.hits, reverse=True)

		return self.plist[:self.limit]

pop_news = PopNews()

class IndexView(generic.ListView):
	template_name = 'news/index.html'
	context_object_name = 'news'
	paginate_by = 10

	def get_queryset(self):
		return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['services'] = Service.objects.all().order_by('index')
		context['pop'] = pop_news.get(context['object_list'])
		return context

class ArticleView(HitCountDetailView):
	model = Article
	template_name = 'news/article.html'
	count_hit = True
	context_object_name = 'article'

	def get_queryset(self):
		"""Excludes any questions that aren't published yet."""
		return Article.objects.filter(pub_date__lte=timezone.now())

	def get_context_data(self, **kwargs):
		context = super(ArticleView, self).get_context_data(**kwargs)
		context['services'] = Service.objects.all().order_by('index')
		context['pop'] = pop_news.get(Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date'))
		return context