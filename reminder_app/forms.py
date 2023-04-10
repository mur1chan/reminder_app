from django.forms import ModelForm
from django import forms
from .models import Reminder

class AddReminder(ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'date', 'time', 'description']
        widgets = {
            'title': forms.TextInput(),
            'date': forms.DateInput(),
            'time': forms.TimeInput(),
            'description': forms.TextInput()
        }

