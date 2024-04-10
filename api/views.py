from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def apiOverview(request):
    return JsonResponse('This is the home page for the API Routes', safe=False)