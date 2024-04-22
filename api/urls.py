
from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns =[
    path('', views.apiOverview, name="api-overview"),
    path("patrons/", views.getPatrons, name="get-patrons"),
    path('patron/<str:pk>/', views.getPatron, name='get-patron'),
    
    
    
    path('transactions/', views.getTransactions, name='get-transactions'),
    path('transaction/<str:pk>/', views.getTransaction, name='get-transaction'),
    
    path('journeys/', views.getJourneys, name='get-journeys'),
    path('journey/<str:pk>/', views.getJourney, name='get-journey'),
    
    path('fares/', views.getFares, name='get-fares'),
    path('fare/<str:pk>/', views.getFare, name='get-fare'),
    
    path('cards/', views.getCards, name='get-cards'),
    path('card/<str:pk>/', views.getCard, name='get-card'),
    
    path('stations/', views.getStations, name='get-stations'),
    path('station/<str:pk>/', views.getStation, name='get-station'),
    
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

