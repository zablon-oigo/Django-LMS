from django import forms
from django.forms.models import inlineformset_factory
from .models import Course,Module

ModuleFormSet=inlineformset_factory(
    Course,
    fields=['title','description'],
    extra=2,
    can_delete=True
)