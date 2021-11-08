from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    """ Products form """

    class Meta:
        """ Product form fields """
        model = Product
        exclude = ('rating',)

    # to validate the form data
    def clean(self):

        # fetch data from form
        super(ProductForm, self).clean()

        # extract the field data
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        on_sale = self.cleaned_data.get('on_sale')
        discount_percent = self.cleaned_data.get('discount_percent')

        # Product name must not have just empty characters and must be
        # > 10 characters long
        if not name:
            self._errors['name'] = self.error_class([
                'Please enter valid text - this field must not be blank or '
                'contain just blank spaces'])
        elif len(name) < 10:
            self._errors['name'] = self.error_class([
                'Minimum of 10 characters required'])
        # Product description must not have just empty characters and must be
        # > 50 characters long
        if not description:
            self._errors['description'] = self.error_class([
                'Please enter valid text - this field must not be blank or '
                'contain just blank spaces'])
        elif len(description) < 50:
            self._errors['description'] = self.error_class([
                'Minimum of 50 characters required'])

        if on_sale is True and not discount_percent:
            self._errors['discount_percent'] = self.error_class([
                'Discount percentage must be included for a product that '
                'is on sale'])

        # return errors in form
        return self.cleaned_data

    image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ReviewForm(forms.ModelForm):
    """ Review form """

    class Meta:
        """ Review form fields """
        model = ProductReview
        fields = (
            'review_rating',
            'review_comment'
        )
