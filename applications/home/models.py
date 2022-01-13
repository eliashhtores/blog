from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    title = models.CharField(max_length=30)
    description = models.TextField()
    about = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    about_text = models.TextField()
    contact_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title


class Subscriber(TimeStampedModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
