from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    """ Products form """

    class Meta:
        model = Product
        exclude = ('rating',)

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class ReviewForm(forms.ModelForm):
    """ Review form """

    class Meta:
        model = ProductReview
        fields = (
            'review_rating',
            'review_comment'
        )

    def clean(self):

        # fetch data from form
        super(ReviewForm, self).clean()

        # extract the field data
        review_comment = self.cleaned_data.get('review_comment')

        # title must not have just empty characters and must be > 10 characters long
        if review_comment is None:
            self._errors['review_comment'] = self.error_class([
                'Please enter valid text'])
        elif len(review_comment) < 10:
            self._errors['review_comment'] = self.error_class([
                'Minimum 10 characters required'])
    
