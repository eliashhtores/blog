from django.db import models


class EntryManager(models.Manager):
    def get_home_cover(self):
        return self.filter(published=True, cover=True).order_by('-created').first()

    def get_home_entries(self):
        return self.filter(published=True, in_home=False).order_by('-created')[:4]

    def get_recent_entries(self):
        return self.filter(published=True).order_by('-created')[:3]
