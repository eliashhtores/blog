from django.db import models


class EntryManager(models.Manager):
    def get_home_cover(self):
        return self.filter(published=True, cover=True).order_by('-created').first()

    def get_home_entries(self):
        return self.filter(published=True, in_home=True).order_by('-created')[:4]

    def get_recent_entries(self):
        return self.filter(published=True, in_home=False, cover=False).order_by('-created')[:3]

    def search_entries(self, title, category):
        if len(category) > 0:
            return self.filter(
                published=True,
                category__id=category,
            ).order_by('-created')

        return self.filter(
            published=True,
            title__icontains=title,
        ).order_by('-created')
