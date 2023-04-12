from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, register, view_login, view_logout
from django.contrib.auth import views as auth_views
from card.views import SnakeDetailView, SnakeListView, SnakeFormView, SearchResultsView, AmphibianListView, AmphibianFormView, AmphibianDetailView

urlpatterns = [
    path('recherche', SearchResultsView, name='search_cards'),


    path('fiches-de-maintiens-serpents/', SnakeListView.as_view(), name="snake_list"),
    path('fiches-de-maintiens-serpents/ajouter/', SnakeFormView.as_view(), name="snake_create"),
    path('fiches-de-maintiens-serpents/<slug:slug>/', SnakeDetailView.as_view(), name='snake_details'),

    path('fiches-de-maintiens-amphibiens/', AmphibianListView.as_view(), name="amphibian_list"),
    path('fiches-de-maintiens-amphibiens/ajouter/', AmphibianFormView.as_view(), name="amphibian_create"),
    path('fiches-de-maintiens-amphibiens/<slug:slug>/', AmphibianDetailView.as_view(), name="amphibian_details"),

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
