"""Post forms."""

# Django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post Model form."""

    class Meta:
        """Form Settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')