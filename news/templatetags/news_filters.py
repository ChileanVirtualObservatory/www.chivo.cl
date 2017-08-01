from django import template
from BeautifulSoup import BeautifulSoup

register = template.Library()

@register.filter(name='removetags')
def removetags(value, arg):
	soup = BeautifulSoup(value)
	[s.extract() for s in soup('img')]
	return soup