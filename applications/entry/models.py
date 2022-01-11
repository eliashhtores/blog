from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


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
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title
