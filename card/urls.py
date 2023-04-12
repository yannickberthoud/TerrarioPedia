from django.urls import path
from .views import CardDetailView, CardListView, About, CardFormView

urlpatterns = [
    path('ajouter/', CardFormView.as_view(), name="add_card"),
    path('a-propos/', About, name='card-about'),
]