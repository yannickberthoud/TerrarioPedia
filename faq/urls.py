from django.urls import path
from .views import FaqListView

urlpatterns = [
    path('', FaqListView.as_view(), name='faq-list'),
]