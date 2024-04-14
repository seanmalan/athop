from rest_framework.serializers import ModelSerializer
from .models import Patron, Transaction, Journey, Fare, Station, Card


class PatronSerializer(ModelSerializer):
    class Meta:
        model = Patron
        fields = '__all__'
        
        
class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        

class JourneySerializer(ModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'
        
        
class FareSerializer(ModelSerializer):
    class Meta:
        model = Fare
        fields = '__all__'
        

class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        
        
class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

