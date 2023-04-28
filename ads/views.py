from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AdsForm
from .models import Ads
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.db.models import Q

class AdsListView(ListView):
    model = Ads
    template_name = 'ads/ads_list.html'
    context_object_name = 'objects'
    queryset = Ads.objects.order_by('-created_at')

class AdsOwnListView(ListView):
    model = Ads
    template_name = 'ads/ads_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return Ads.objects.order_by('-created_at').filter(owner=self.request.user.pk)

@method_decorator(login_required, name='dispatch')
class AdsDetailsView(DetailView):
    model = Ads
    template_name = 'ads/ads_details.html'
    context_object_name = 'object'

@method_decorator(login_required, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    form_class = AdsForm
    template_name = "ads/form.html"  # Replace with your template.

    def get_success_url(self):
        return reverse('ads_details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            self.object.images.create(image=image)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = reverse_lazy("ads_list")

@method_decorator(login_required, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    form_class = AdsForm
    template_name = "ads/form.html"  # Replace with your template.

    def get_success_url(self):
        return reverse('ads_details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            self.object.images.create(image=image)
        return super().form_valid(form)

def SearchAdsResultsView(request):
    if request.method == "POST":
        type_of_ads = request.POST["type_of_ads"]
        search = request.POST["query"]
        category = request.POST["category"]

        query = Ads.objects.filter(Q(type_of_ads__contains=type_of_ads) & Q(description__icontains=search) & Q(category__contains=category)).order_by('-created_at')

        return render(request, 'ads/ads_list.html', {'objects': query, 'query': search})
