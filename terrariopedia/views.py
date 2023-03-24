from django.shortcuts import render
from card.models import Card


def home(request):
    cards = Card.objects.order_by('genus', 'species')[:15]
    return render(request, 'terrariopedia/home.html', {'cards': cards})
