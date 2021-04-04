from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'title_image',
                  'short_description', 'blog_content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_content': forms.Textarea(attrs={'class': 'form-control'}),


        }
