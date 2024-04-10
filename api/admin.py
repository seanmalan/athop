from django.contrib import admin

# Register your models here.
from .models import Patron, Transaction, Journey, Fare, Station, Card

admin.site.register(Patron)
admin.site.register(Transaction)
admin.site.register(Journey)
admin.site.register(Fare)
admin.site.register(Station)
admin.site.register(Card)
