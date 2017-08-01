from django import forms
from django.contrib import admin

from .models import Person, History, Institution, Datacenter, Service, SubService, Paper, Thesis

# ====================
#       PERSONS
# ====================
class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'area','image')
	list_filter = ['name', 'area']
	search_fields = ['name', 'area']
	fields = ['name','email','gender','area','link','position','image','projects','biography']

admin.site.register(Person, PersonAdmin)

# ====================
#       HISTORY
# ====================
class HistoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	list_filter = ['title', 'date']
	search_fields = ['title', 'date']
	fields = ['title','date','content']

admin.site.register(History, HistoryAdmin)

# ====================
#     INSTITUTION
# ====================
class InstitutionAdmin(admin.ModelAdmin):
	list_display = ('name', 'link', 'image')
	list_filter = ['name']
	search_fields = ['name', 'link']
	fields = ['name', 'link', 'image']

admin.site.register(Institution, InstitutionAdmin)

# ====================
#      DATACENTER
# ====================
class DatacenterAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ['title']
	search_fields = ['title']
	fields = ['title','content']

admin.site.register(Datacenter, DatacenterAdmin)

# ====================
#       SERVICE
# ====================
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name','index','link')
	list_filter = ['name','link']
	search_fields = ['name','link']
	fields = ['name','index','link','content']

admin.site.register(Service, ServiceAdmin)

# ====================
#     SUBSERVICE
# ====================
class CustomServiceChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name

class SubServiceForm(forms.ModelForm):
	service = CustomServiceChoiceField(queryset=Service.objects.all())
	class Meta:
		model = SubService
		fields = ['name','index','link','service','image','content']
		exclude = []

class SubServiceAdmin(admin.ModelAdmin):
	list_display = ('name','link','servicio','index')
	list_filter = ['name','link']
	search_fields = ['name','link','servicio']
	form = SubServiceForm

	def servicio(self, obj):
		return obj.service.name

admin.site.register(SubService, SubServiceAdmin)

# ====================
#      DOCUMENTS
# ====================

class PaperAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date', 'university', 'link')
	list_filter = ['title', 'author', 'date', 'university']
	search_fields = ['title', 'date', 'university']
	fields = ['title', 'author', 'date', 'link', 'university', 'description']

admin.site.register(Paper, PaperAdmin)

class ThesisAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date', 'university', 'file')
	list_filter = ['title', 'author', 'date', 'university']
	search_fields = ['title', 'date', 'university']
	fields = ['title', 'author', 'date', 'file', 'university', 'info', 'description']

admin.site.register(Thesis, ThesisAdmin)