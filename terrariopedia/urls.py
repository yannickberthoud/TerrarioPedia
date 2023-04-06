from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, register, view_login, view_logout
from django.contrib.auth import views as auth_views
from card.views import SearchResultsView

urlpatterns = [
    path('petites-annonces/', include('ads.urls')),
    path('recherche', SearchResultsView, name='search_cards'),
    path('fiches-de-maintiens/', include(('card.urls', 'card'), namespace="card-link")),
    path('faq', include('faq.urls')),
    path('admin/', admin.site.urls),
    path('informations/', include('django.contrib.flatpages.urls')),
    path('', home, name='home'),
    path("register", register, name="register"),
    path("login", view_login, name="login"),
    path("logout", view_logout, name="logout"),
    path("profile/", include('member.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap,
        {'sitemaps': {'flatpages': FlatPageSitemap}},
        name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
