from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Patron, Transaction, Journey, Fare, Station, Card
from .serializers import PatronSerializer, TransactionSerializer, JourneySerializer, FareSerializer, StationSerializer, CardSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    
    routes = {
        'Patrons': '/patrons',
        'Transactions': '/transactions',
        'Journeys': '/journeys',
        'Fares': '/fares',
        'Stations': '/stations',
        'Cards': '/cards',
    }
    
    return Response(routes)

@api_view(['GET'])
def getPatrons(request):
    patrons = Patron.objects.all()
    serializer = PatronSerializer(patrons, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getPatron(request, pk):
    try:
        patron = Patron.objects.get(pk=pk)
    except Patron.DoesNotExist:
        return Response({"error": "Patron not found"}, status=404)
    
    transactions = Transaction.objects.filter(patron=patron)
    journeys = Journey.objects.filter(patron=patron)
    cards = Card.objects.filter(patron=patron)
    
    patron_serializer = PatronSerializer(patron)
    transaction_serializer = TransactionSerializer(transactions, many=True)
    journey_serializer = JourneySerializer(journeys, many=True)
    card_serializer = CardSerializer(cards, many=True)
    
    context = {
        "patron": patron_serializer.data,
        "transactions": transaction_serializer.data,
        "journeys": journey_serializer.data,
        "cards": card_serializer.data
    }
    
    return Response(context)





@api_view(['GET'])
def getTransactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getTransaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getJourneys(request):
    journeys = Journey.objects.all()
    serializer = JourneySerializer(journeys, many=True)
    return Response(serializer.data)





@api_view(['GET'])
def getJourney(request, pk):
    journey = Journey.objects.get(id=pk)
    serializer = JourneySerializer(journey, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def getFares(request):
    fares = Fare.objects.all()
    serializer = FareSerializer(fares, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getFare(request, pk):
    fare = Fare.objects.get(id=pk)
    serializer = FareSerializer(fare, many=False)
    return Response(serializer.data)






@api_view(['GET'])
def getStations(request):
    stations = Station.objects.all()
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)






@api_view(['GET'])
def getStation(request, pk):
    station = Station.objects.get(id=pk)
    serializer = StationSerializer(station, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getCards(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getCard(request, pk):
    card = Card.objects.get(id=pk)
    serializer = CardSerializer(card, many=False)
    return Response(serializer.data)
