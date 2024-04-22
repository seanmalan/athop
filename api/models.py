from django.db import models

# Create your models here.

class Patron(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

      
class Transaction(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    amount = models.FloatField()
    original_balance = models.FloatField()
    new_balance = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patron.first_name} {self.patron.last_name} - Amount: {self.amount}'

      
class Journey(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patron.first_name} {self.patron.last_name} - {self.start_location} to {self.end_location}'



class Fare(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return f'{self.start_location} to {self.end_location} - Amount: {self.amount}'

class Card(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='cards')
    card_number = models.IntegerField()
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f'Card {self.card_number} - Balance: {self.balance}'

      
class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)

    def __str__(self):
        return self.name



