from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import Card, Amphibian
from .forms import SnakeForm, AmphibianForm

class AmphibianListView(ListView):
    model = Amphibian
    template_name = 'card/amphibian_list.html'
    context_object_name = 'objects'

class AmphibianDetailView(DetailView):
    model = Amphibian
    template_name = 'card/amphibian_details.html'
    context_object_name = 'object'

class SnakeDetailView(DetailView):
    model = Card
    template_name = 'card/snake_details.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

class SnakeListView(ListView):
    model = Card
    template_name = 'card/snake_list.html'
    context_object_name = 'objects'

def SearchResultsView(request):
    if request.method == "POST":
        query = request.POST["query"]
        listing = query.split(" ", 1)
        genus = listing[0].capitalize()

        if len(listing) > 1:
            species = listing[1]
            snakes = Card.objects.filter(Q(genus__contains=genus) | Q(species__contains=species)).order_by('genus', 'species')
            amphibians = Amphibian.objects.filter(Q(genus__contains=genus) | Q(species__contains=species)).order_by('genus', 'species')
        else:
            snakes = Card.objects.filter(Q(genus__contains=genus) | Q(species__contains=genus)).order_by('genus', 'species')
            amphibians = Amphibian.objects.filter(Q(genus__contains=genus) | Q(species__contains=genus)).order_by('genus','species')
        return render(request, 'card/list.html', {'snakes': snakes, 'amphibians': amphibians, 'query': query})
def About(request):
    return render(request, 'card/about.html')

@method_decorator(login_required, name='dispatch')
class SnakeFormView(CreateView):
    model = Card
    form_class = SnakeForm
    template_name = 'card/snake_form.html'
    def get_success_url(self):
        return reverse('snake_details', kwargs={'slug': self.object.slug})

@method_decorator(login_required, name='dispatch')
class AmphibianFormView(CreateView):
    model = Amphibian
    form_class = AmphibianForm
    template_name = 'card/amphibian_form.html'
    def get_success_url(self):
        return reverse('amphibian_details', kwargs={'slug': self.object.slug})