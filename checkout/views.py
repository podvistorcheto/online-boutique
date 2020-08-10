from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import Orderform

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HDOLVLVB4v4eSDr59suh8eAYNpAHN4UQpFkGC53RHABUiRlPOjjAtgzSfQIVfm5gTKOqGQGbFSRTKrJLCsXYxmQ00xgRmGPUa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)