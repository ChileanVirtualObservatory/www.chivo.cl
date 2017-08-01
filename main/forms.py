from django import forms
from django.contrib.auth.models import User

from .models import Service, SubService


class CustomServiceChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name


class SubServiceForm(forms.ModelForm):
    service = CustomServiceChoiceField(queryset=Service.objects.all())

    class Meta:
        model = SubService