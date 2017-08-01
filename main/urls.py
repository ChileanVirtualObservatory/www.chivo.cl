from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^history$', views.HistoryView.as_view(), name='history'),
	url(r'^services$', views.ServicesView.as_view(), name='services'),
	url(r'^datacenter$', views.DatacenterView.as_view(), name='datacenter'),
	url(r'^staff$', views.StaffView.as_view(), name='staff'),
	url(r'^documents$', views.DocumentsView.as_view(), name='documents'),
]