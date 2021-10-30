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
        content_two = self.cleaned_data.get('content_two')
        content_three = self.cleaned_data.get('content_three')

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
        if content_one is None:
            self._errors['content_one'] = self.error_class([
                'Please enter valid text'])
        elif len(content_one) < 50:
            self._errors['content One'] = self.error_class([
                'Minimum 50 characters required'])

        if content_two is None:
            self._errors['content_two'] = self.error_class([
                'Please enter valid text'])

        if content_three is None:
            self._errors['content_three'] = self.error_class([
                'Please enter valid text'])

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
