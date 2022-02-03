from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KOpwVBFR7XqHEARdX3QBwbSTtFnHDrJqijr2n8xHEPnUkGY74YmZ3KcxzzxBHTCs3j9ibnGnH7kRPAZRh4CZHi200Jb0fok87',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
