from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    """ Form for creation of blog entry """

    class Meta:
        """ blog form fields """
        model = BlogPost
        fields = (
            'author',
            'title',
            'intro',
            'content_one',
            'content_two',
            'content_three',
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
        content_one = self.cleaned_data.get('content_one')

        # Blog title must not have just empty characters and must be
        # > 5 characters long
        if not title:
            self._errors['title'] = self.error_class([
                'Please enter valid text - this field must not be blank'])
        elif len(title) < 5:
            self._errors['title'] = self.error_class([
                'Minimum of 5 characters required'])
        # Blog intro must not have just empty characters and must be
        # > 5 characters long
        if not intro:
            self._errors['intro'] = self.error_class([
                'Please enter valid text - this field must not be blank'])
        elif len(intro) < 10:
            self._errors['intro'] = self.error_class([
                'Minimum of 10 characters required'])
        # title must not have just empty characters and must be
        # > 50 characters long
        if not content_one:
            self._errors['content_one'] = self.error_class([
                'Please enter valid text - this field must not be blank'])
        elif len(content_one) < 50:
            self._errors['content_one'] = self.error_class([
                'Minimum of 50 characters required'])

        # return errors in form
        return self.cleaned_data

    image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """ Comment form for blog comments """
    class Meta:
        """ Blog comment form fields """

        model = BlogComment
        fields = (
            'comment_title',
            'comment',
            )
