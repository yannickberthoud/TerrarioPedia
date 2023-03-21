from django.views.generic import ListView
from .models import Faq

class FaqListView(ListView):
    model = Faq
    template_name = 'faq/list.html'
    context_object_name = 'questions'
    queryset = Faq.objects.order_by('category')
