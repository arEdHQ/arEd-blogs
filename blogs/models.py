from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
# for avg time
from .utils import get_read_time
import math

# Create your models here.


class Blog(models.Model):
    # fields for blogs form
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_image = models.ImageField(
        upload_to='blog/',
        help_text='This image will be displayed as the title image of the blog.'
    )
    short_description = models.TextField()
    blog_content = RichTextUploadingField()
    published_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    blog_views = models.IntegerField(default=0)
    blog_likes = models.ManyToManyField(User, related_name='likes')
    read_time = models.TimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            if Blog.objects.filter(title=(self.title)).exists():
                count = Blog.objects.filter(title=(self.title)).count()
                self.slug = "%s-%s" % (slugify(kwargs.pop('title',
                                                          self.title)), count+1)
            else:
                self.slug = slugify(kwargs.pop('title', self.title))
        return super(Blog, self).save(*args, **kwargs)

# this redirects post button to blog-detail page
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def number_of_likes(self):
        return self.blog_likes.count()

    def blog_readtime(self):
        html_string = self.blog_content
        read_time_var = get_read_time(html_string)
        self.read_time = read_time_var
        return math.ceil(read_time_var)

    def get_api_like_url(self):
        return reverse("blogs:blogpost_api_like", kwargs={"slug": self.slug})
