from django.urls import path
from .views import AdsListView,AdsDetailsView, adsFormView

urlpatterns = [
    path('<int:pk>', AdsDetailsView.as_view(), name='ads-details'),
    path('ajouter/', adsFormView, name="ads-create"),
    path('', AdsListView.as_view(), name='ads'),
]