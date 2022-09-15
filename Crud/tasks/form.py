from django import forms
from django.forms import ModelForm

from .models import task


class TaskForm (ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a decription'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto mb-2'}),
        }
