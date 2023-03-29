from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from django.contrib.auth import views as auth_views
from card.views import SearchResultsView

urlpatterns = [
    path('recherche', SearchResultsView, name='search_cards'),
    path('fiches-de-maintiens/', include('card.urls')),
    path('faq', include('faq.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
