from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
from .models import Ads
from .forms import AdsForm, AdsImageForm

class AdsDetailsView(DetailView):
    model = Ads
    template_name = 'ads/details.html'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

class AdsListView(ListView):
    model = Ads
    template_name = 'ads/list.html'
    context_object_name = 'ads'
    queryset = Ads.objects.order_by('created_at')

@login_required
def adsFormView(request):
    if request.method == 'POST':
        ads_form = AdsForm(request.POST, instance=request.user)
        ads_image_form = AdsImageForm(request.POST, instance=request.ads)
        if ads_form.is_valid() and ads_image_form.is_valid():
            ads_form.save()
            ads_image_form.save()
            messages.success(request, 'Votre annonce a été publié.')
            return redirect(to='profile')
    else:
        ads_form = AdsForm(instance=request.user)
        ads_image_form = AdsImageForm(instance=request.user)

    return render(request, 'ads/form.html', {'ads_form': ads_form, 'ads_image_form': ads_image_form})