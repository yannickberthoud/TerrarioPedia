from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Suggestion
from .forms import SuggestionForm

class SuggestionListView(ListView):
    model = Suggestion
    template_name = 'suggestion/suggestion_list.html'
    context_object_name = 'objects'
    queryset = Suggestion.objects.order_by('-created_at', 'treaty')

@method_decorator(login_required, name='dispatch')
class SuggestionDetailView(DetailView):
    model = Suggestion
    template_name = 'suggestion/suggestion_details.html'
    context_object_name = 'object'

@method_decorator(login_required, name='dispatch')
class SuggestionCreateView(CreateView):
    model = Suggestion
    form_class = SuggestionForm
    template_name = 'suggestion/suggestion_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('suggestion_details', kwargs={'pk': self.object.pk})