from django.db import models
from django.conf import settings
from applications.entry.models import Entry

from model_utils.models import TimeStampedModel


class Favorite(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_favorite", on_delete=models.CASCADE)
    entry = models.ForeignKey(
        Entry, related_name="entry_favorite", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'entry')

    def __str__(self):
        return self.entry.title
