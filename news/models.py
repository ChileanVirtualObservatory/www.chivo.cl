from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from hitcount.models import HitCount

from BeautifulSoup import BeautifulSoup

class Article(models.Model):
	title = models.CharField('Titulo',max_length=200)
	image = RichTextUploadingField()
	pub_date = models.DateTimeField('Fecha de Publicacion')
	content = RichTextUploadingField('Texto')
	#user = models.ForeignKey(settings.AUTH_USER_MODEL)
	#hits = models.ForeignKey(HitCount)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		soup = BeautifulSoup(self.content)
		list = soup.findAll('img')
		if len(list) > 0:
			self.image = soup.findAll('img')[0]['src']
		super(Article, self).save(force_insert, force_update, using, update_fields)