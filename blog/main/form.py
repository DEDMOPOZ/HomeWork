from .models import Post

from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short Description',
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            })
        }

