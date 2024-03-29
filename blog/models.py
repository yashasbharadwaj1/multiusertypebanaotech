from django.db import models
from django.utils import timezone
from multiusertype.models import User
from django.urls import reverse
import random
import string


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(publish_status='P')

    # options = (
    # ('draft', 'Draft'),
    # ('published', 'Published'),
    # )

    title = models.CharField(max_length=250)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts', default=4)

    postimg = models.ImageField(upload_to='post_images', default='Success.png')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    summary = models.TextField(blank=False, default='some summary')
    content = models.TextField(blank=False, default='some content')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    publish_status = models.CharField(max_length=15, default='pub')
    draft_status = models.CharField(max_length=15, default='draf')

    newmanager = NewManager()  # custom manager
    objects = models.Manager()  # default manager

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


