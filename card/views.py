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
        listing = query.split(" ", 1)
        genus = listing[0]

        if len(listing) > 1:
            species = listing[1]
            cards = Card.objects.filter(Q(genus__contains=genus) | Q(species__contains=species)).order_by('genus', 'species')
        else:
            cards = Card.objects.filter(Q(genus__contains=genus) | Q(species__contains=genus)).order_by('genus', 'species')
        return render(request, 'card/list.html', {'cards': cards, 'query': query})

def FilterGenusListView(request):
    if request.method == "POST":
        query = request.POST['sFilterGenus']
        if query != "all":
            cards = Card.objects.filter(Q(genus__contains=query)).order_by('genus', 'species')
        else:
            cards = Card.objects.order_by('genus', 'species')

        return render(request, 'card/list.html', {'cards': cards, 'query': query})
def About(request):
    return render(request, 'card/about.html')