from .models import Kollektsioon, Toode
import stripe
from django.conf import settings
from django.shortcuts import render, redirect

def kollektsioonid(request):
    kollektsioonid = Kollektsioon.objects.all()
    return render(request, 'galerii/kollektsioonid.html', {'kollektsioonid': kollektsioonid})

def tooted(request):
    tooted = Toode.objects.filter(saadaval=True)
    return render(request, 'galerii/tooted.html', {'tooted': tooted})

def kontakt(request):
    return render(request, 'galerii/kontakt.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request, toode_id):
    toode = Toode.objects.get(id=toode_id)
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': toode.nimi},
                'unit_amount': int(toode.hind * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )

    return redirect(checkout_session.url)

def success(request):
    return render(request, 'galerii/success.html')

def cancel(request):
    return render(request, 'galerii/cancel.html')

def home(request):
    kollektsioonid = Kollektsioon.objects.all()
    tooted = Toode.objects.filter(saadaval=True)
    return render(request, 'home.html', {'kollektsioonid': kollektsioonid, 'tooted': tooted})
