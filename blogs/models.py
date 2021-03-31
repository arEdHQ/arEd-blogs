from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title_image = models.ImageField(
#         upload_to = 'blog/',
#         blank=True,
#         null=True,
#         default='blog/default.png',
#         help_text = 'This image will be displayed as the title image of the blog.'
#     )
    short_description = models.TextField()
    blog_content = RichTextUploadingField()
#    published_date = models.DateTimeField(auto_now_add=True)
    blog_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=(str(self.id)))
