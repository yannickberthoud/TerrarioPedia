from django.shortcuts import render
from card.models import Card


def home(request):
    cards = Card.objects.order_by('genus', 'species')[:16]
    return render(request, 'terrariopedia/home.html', {'cards': cards})
