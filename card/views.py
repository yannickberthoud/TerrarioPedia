from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import Card, Amphibian, Lizard
from .forms import SnakeForm, AmphibianForm, LizardForm


class AmphibianListView(ListView):
    model = Amphibian
    template_name = 'card/amphibian_list.html'
    context_object_name = 'objects'
    queryset = Amphibian.objects.order_by('genus', 'species')

class LizardListView(ListView):
    model = Lizard
    template_name = 'card/lizard_list.html'
    context_object_name = 'objects'
    queryset = Lizard.objects.order_by('genus', 'species')

class AmphibianDetailView(DetailView):
    model = Amphibian
    template_name = 'card/amphibian_details.html'
    context_object_name = 'object'

class LizardDetailView(DetailView):
    model = Lizard
    template_name = 'card/lizard_details.html'
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
    queryset = Card.objects.order_by('genus', 'species')

def SearchResultsView(request):
    if request.method == "POST":
        query = request.POST["query"]
        snakes = Card.objects.filter(Q(genus__icontains=query) | Q(species__icontains=query)).order_by('genus', 'species')
        amphibians = Amphibian.objects.filter(Q(genus__icontains=query) | Q(species__icontains=query)).order_by('genus', 'species')
        lizards = Lizard.objects.filter(Q(genus__icontains=query) | Q(species__icontains=query)).order_by('genus', 'species')
        return render(request, 'card/search.html', {'snakes': snakes, 'query': query, 'amphibians':amphibians, 'lizards':lizards}) #'amphibians': amphibians, 'query': query})
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

@method_decorator(login_required, name='dispatch')
class LizardFormView(CreateView):
    model = Lizard
    form_class = LizardForm
    template_name = 'card/lizard_form.html'
    def get_success_url(self):
        return reverse('lizard_details', kwargs={'slug': self.object.slug})