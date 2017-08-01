# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import os
import hashlib

def sha1_file(file_path):
	# BUF_SIZE is totally arbitrary, change for your app!
	BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
	sha1 = hashlib.sha1()
	with open(file_path, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			sha1.update(data)
	return sha1.hexdigest()

'''
def profile_image_directory_path(instance, filename):
	file_path = os.path.join(settings.MEDIA_ROOT, "profile-images/", str(filename))
	file_sha1 = sha1_file(file_path)
	file_ext  = "."+os.path.splitext(filename)[1][1:].strip().lower()
	file_path = os.path.join(settings.MEDIA_ROOT, "profile-images/", file_sha1+file_ext)

	is_file = os.path.exists(file_path)
	if is_file:
		os.remove(file_path)
	return "profile-images/"+str(filename)
'''
def profile_image_directory_path(instance, filename):
	return "profile-images/"+str(filename)

# Create your models here.
class Person(models.Model):
	TYPECHOICE = (('0', 'Directivo'), ('1', 'Cientifico'), ('2', 'Tecnico'), )
	GENDERCHOICE = (('0', 'Mujer'), ('1', 'Hombre'), )

	name = models.CharField('Nombre', max_length=60, blank=False)
	email = models.CharField('Email', max_length=60, blank=True, default='')
	position = models.CharField('Cargo', max_length=60, blank=False, default='')
	image = models.ImageField('Imagen', upload_to=profile_image_directory_path, blank=True, null=True)
	area = models.CharField('Tipo/Area', max_length=1, choices=TYPECHOICE)
	gender = models.CharField('Genero', max_length=1, choices=GENDERCHOICE, default=1)
	projects = RichTextUploadingField('Proyectos', default='', blank=True)
	biography = RichTextUploadingField('Mini-Biografia', default='', blank=True)
	link = models.URLField('Enlace Web Personal', max_length=500, blank=True, null=False, default='')

	def clean(self):
		if self.name == '' or self.position == '':
			raise ValidationError('Empty error message')


def institution_image_directory_path(instance, filename):
	return "institution-images/"+str(filename)

class Institution(models.Model):
	name = models.CharField('Nombre', max_length=60, blank=False)
	link = models.URLField('Enlace', max_length=500, blank=True, null=True)
	image = models.ImageField('Imagen', upload_to=institution_image_directory_path, blank=False, null=False)

	def clean(self):
		if self.name == '' or self.image == '':
			raise ValidationError('Empty error message')

class History(models.Model):
	title = models.CharField('Titulo', max_length=200, blank=False)
	date = models.DateTimeField('Date')
	content = RichTextUploadingField('Texto')

	def clean(self):
		if self.title == '' or self.date == '' or self.content == '':
			raise ValidationError('Empty error message')

class Datacenter(models.Model):
	title = models.CharField('Titulo', max_length=200, blank=False)
	content = RichTextUploadingField('Texto')

	def clean(self):
		if self.title == '' or self.content == '':
			raise ValidationError('Empty error message')

class Service(models.Model):
	index = models.PositiveSmallIntegerField('Indice de Ordenamiento', default=0)
	name = models.CharField('Nombre', max_length=200, blank=False)
	link = models.URLField('Enlace', max_length=500, blank=True, null=True)
	content = RichTextUploadingField('Descripcion')

	def clean(self):
		if self.name == '':
			raise ValidationError('Empty error message')


def service_image_directory_path(instance, filename):
	return "service-images/"+str(filename)

class SubService(models.Model):
	index = models.PositiveSmallIntegerField('Indice de Ordenamiento', default=0)
	name = models.CharField('Nombre', max_length=200, blank=False)
	link = models.URLField('Enlace', max_length=500, blank=True, null=True)
	image = models.ImageField('Imagen', upload_to=service_image_directory_path, blank=True, null=True)
	content = RichTextUploadingField('Descripcion',blank=True)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)

	def clean(self):
		if self.name == '' or self.content == '':
			raise ValidationError('Empty error message')

class Paper(models.Model):
	title = models.CharField('Titulo', max_length=200, blank=False)
	author = models.CharField('Autor(es)', max_length=300, blank=False)
	date = models.DateTimeField('Fecha de Publicacion', blank=False)
	link = models.URLField('Enlace', max_length=500, blank=True, null=False, default='')
	description = RichTextUploadingField('Descripcion',blank=False)
	university = models.CharField('Universidad', max_length=200, blank=True, default='')

	def clean(self):
		if self.title == '' or self.description == '' or self.author == '' or self.date == '':
			raise ValidationError('Empty error message')

def thesis_doc_directory_path(instance, filename):
	return "thesis-files/"+str(filename)

class Thesis(models.Model):
	title = models.CharField('Titulo', max_length=200, blank=False)
	author = models.CharField('Autor(es)', max_length=200, blank=False)
	date = models.DateTimeField('Fecha de Publicacion', blank=False)
	info = RichTextUploadingField('Informacion', blank=False)
	file = models.FileField('Archivo', upload_to=thesis_doc_directory_path, blank=False, null=True)
	description = RichTextUploadingField('Descripcion', blank=False)
	university = models.CharField('Universidad', max_length=200, blank=True, default='')

	def clean(self):
		if self.title == '' or self.description == '' or self.date == '' or self.author == '' or self.info == '':
			raise ValidationError('Empty error message')
