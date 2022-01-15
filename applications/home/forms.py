from django import forms
from django.forms import widgets
from .models import Subscriber, Contact


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
