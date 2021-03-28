from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField()
    blog_content = RichTextField()
    #likes = models.ManyToManyField(User, related_name='blogpost_like')
    blog_views = models.IntegerField(default=0)

    # def number_of_likes(self):
    #     return self.likes.Count()

    def __str__(self):
        return self.title
