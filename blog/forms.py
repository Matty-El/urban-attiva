from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    """ Form for creation of blog entry """

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

    # to validate the form data
    def clean(self):

        # fetch data from form
        super(BlogForm, self).clean()

        # extract the field data
        title = self.cleaned_data.get('title')
        intro = self.cleaned_data.get('intro')
        content = self.cleaned_data.get('content')

        # title must not have just empty characters and must be > 5 characters long
        if title is None:
            self._errors['title'] = self.error_class([
                'Please enter valid text'])
        elif len(title) < 5:
            self._errors['title'] = self.error_class([
                'Minimum 5 characters required'])
        # title must not have just empty characters and must be > 50 characters long
        if intro is None:
            self._errors['intro'] = self.error_class([
                'Please enter valid text'])
        elif len(intro) < 5:
            self._errors['intro'] = self.error_class([
                'Minimum 5 characters required'])
        # title must not have just empty characters and must be > 50 characters long
        if content is None:
            self._errors['content'] = self.error_class([
                'Please enter valid text'])
        elif len(content) < 50:
            self._errors['content'] = self.error_class([
                'Minimum 50 characters required'])

        # return errors in form
        return self.cleaned_data

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-full'


class CommentForm(forms.ModelForm):
    """ Comment form for blog comments """

    class Meta:
        model = BlogComment
        fields = (
            'comment_title',
            'comment',
            )
