from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    
    title = models.CharField(max_length=250)
    postimg=models.ImageField(upload_to='post_images',default='Success.png')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)   
    summary = models.TextField(null=True)
    content = RichTextUploadingField(blank=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=10, choices=options, default='draft')
    newmanager = NewManager()  # custom manager
    objects = models.Manager()  # default manager
    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
