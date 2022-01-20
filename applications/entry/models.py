from datetime import timedelta, datetime
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager


class Category(TimeStampedModel):
    short_name = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.short_name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = RichTextUploadingField()
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True)
    cover = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(max_length=300, editable=False)

    objects = EntryManager()

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

    def save(self):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour, minutes=now.minute, seconds=now.second)
        self.slug = slugify('%s %s' % (self.title, int(total_time.seconds)))
        super(Entry, self).save()

    def get_absolute_url(self):
        return reverse_lazy('entry_app:detail', kwargs={'slug': self.slug})
