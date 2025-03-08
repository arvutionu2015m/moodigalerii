from django.db import models
from django.contrib.auth.models import User

class Disainer(models.Model):
    kasutaja = models.OneToOneField(User, on_delete=models.CASCADE)
    nimi = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profiilipilt = models.ImageField(upload_to='disainerid/', blank=True, null=True)

    def __str__(self):
        return self.nimi

class Kollektsioon(models.Model):
    nimi = models.CharField(max_length=100)
    kirjeldus = models.TextField()
    disainer = models.ForeignKey(Disainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.nimi

class Toode(models.Model):
    nimi = models.CharField(max_length=100)
    kirjeldus = models.TextField()
    hind = models.DecimalField(max_digits=10, decimal_places=2)
    kollektsioon = models.ForeignKey(Kollektsioon, on_delete=models.CASCADE)
    pilt = models.ImageField(upload_to='tooted/')
    pilt_360 = models.FileField(upload_to='tooted/360/', blank=True, null=True)
    saadaval = models.BooleanField(default=True)

    def __str__(self):
        return self.nimi
