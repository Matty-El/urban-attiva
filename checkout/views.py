from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, 'There is nothing in your shopping cart at the moment.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JVBSVEsj4vwHVvJbPaUJJi3IMoXIbcKZOlh1rvRgyaTgdUZILcDmUvUkKXd4oIJlL5cNgr6EOPEchjo9Z8LgcEd00RNBjxge3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
