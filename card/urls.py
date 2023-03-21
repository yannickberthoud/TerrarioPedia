from django.urls import path
from .views import CardDetailView, CardListView, CategoryListView, About

urlpatterns = [
    path('a-propos/', About, name='card-about'),
    path('<slug:category>/<slug:slug>/', CardDetailView.as_view(), name='card-details'),
    path('<slug:category>/', CategoryListView.as_view(), name='card-category-list'),
    path('', CardListView.as_view(), name='card-list'),
]