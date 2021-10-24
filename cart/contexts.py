from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if product.on_sale is True:
                total += item_data * Decimal(product.price - ((product.price * product.discount_percent) / 100))
            else:
                total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                if product.on_sale is True:
                    total += quantity * Decimal(product.price - ((product.price * product.discount_percent) / 100))
                else:
                    total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    if request.user.is_authenticated:
        user_discount = total * -Decimal(settings.REGISTERED_USER_DISCOUNT_PERCENTAGE / 100)
    else:
        user_discount = 0

    grand_total = shipping + user_discount + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'user_discount': user_discount,
        'registered_user_discount_percentage': settings.REGISTERED_USER_DISCOUNT_PERCENTAGE,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
