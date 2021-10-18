from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            'author',
            'title',
            'intro',
            'content',
            'image_url',
            'image',
            )

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-full'


class CommentForm(forms.ModelForm):
    """ Comment form for blog comments """

    class Meta:
        # which model and which fields
        model = BlogComment
        fields = (
            'comment_title',
            'comment',
            )
