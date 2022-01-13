from django import forms
from django.forms import widgets
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }
