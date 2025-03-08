from django.urls import path
from .views import home, checkout, kollektsioonid, tooted, kontakt, success, cancel

urlpatterns = [
    path('', home, name='home'),
    path('checkout/<int:toode_id>/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('kollektsioonid/', kollektsioonid, name='kollektsioonid'),
    path('tooted/', tooted, name='tooted'),
    path('kontakt/', kontakt, name='kontakt'),
]
