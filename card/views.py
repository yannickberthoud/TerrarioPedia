from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Q
from .models import Card


class CardDetailView(DetailView):
    model = Card
    template_name = 'card/details.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

class CardListView(ListView):
    model = Card
    template_name = 'card/list.html'
    context_object_name = 'cards'
    queryset = Card.objects.order_by('genus', 'species')

class CategoryListView(ListView):
    model = Card
    template_name = 'card/list.html'
    context_object_name = 'cards'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(category__slug=self.kwargs['category']).order_by('genus', 'species')

def SearchResultsView(request):
    if request.method == "POST":
        query = request.POST["q"]
        cards = Card.objects.filter(Q(genus__startswith=query) | Q(species__startswith=query)).order_by('genus', 'species')
        return render(request, 'card/list.html', {'cards': cards, 'query': query})

def About(request):
    return render(request, 'card/about.html')