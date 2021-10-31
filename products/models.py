from decimal import Decimal
from django.db.models import Avg
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Category(models.Model):
    """ Category model """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


SIZE_OPTIONS = (
        ('UK 4', 'UK 4'),
        ('UK 4.5', 'UK 4.5'),
        ('UK 5', 'UK 5'),
        ('UK 5.5', 'UK 5.5'),
        ('UK 6', 'UK 6'),
        ('UK 6.5', 'UK 6.5'),
        ('UK 7', 'UK 7'),
        ('UK 7.5', 'UK 7.5'),
        ('UK 8', 'UK 8'),
        ('UK 8.5', 'UK 8.5'),
        ('UK 9', 'UK 9'),
        ('UK 9.5', 'UK 9.5'),
        ('UK 10', 'UK 10'),
        ('UK 10.5', 'UK 10.5'),
        ('UK 11', 'UK 11'),
        ('UK 11.5', 'UK 11.5'),
        ('UK 12', 'UK 12'),
        ('UK 12.5', 'UK 12.5'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    discount_percent = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    size = MultiSelectField(
        choices=SIZE_OPTIONS, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def product_sale_price(self):
        """ Calculate sale price of product """
        product_sale_price = Decimal(self.price -
                                     ((self.price * self.discount_percent) /
                                      100))
        return product_sale_price

    # code with stein
    def get_rating(self):
        """ Calculate average product review rating from reviews """
        total = sum(int(review['review_rating']) for review in
                    self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0

    def save_average_product_rating(self):
        """
        Calculate average product rating and update product data
        """
        self.rating = self.reviews.all().aggregate(
            Avg("review_rating"))['review_rating__avg']
        self.save()


RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )


class ProductReview(models.Model):
    """ Product review model """
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews',
                             on_delete=models.CASCADE)
    review_comment = models.TextField(max_length=250, blank=True, null=True)
    review_rating = models.IntegerField(choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
