from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	fields = ['title', 'pub_date', 'content']

admin.site.register(Article, ArticleAdmin)