from django.contrib import admin
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, register, view_login, view_logout
from django.contrib.auth import views as auth_views
from card.views import SnakeDetailView, SnakeListView, SnakeFormView, SearchResultsView, AmphibianListView, AmphibianFormView, AmphibianDetailView, \
    LizardListView, LizardDetailView, LizardFormView

from suggestion.views import SuggestionListView, SuggestionDetailView, SuggestionCreateView
from member.views import CommunityListView, CommunityDetailView

from ads.views import AdsListView, AdsDetailsView, AdsCreateView, AdsUpdateView, AdsDeleteView, AdsOwnListView, SearchAdsResultsView


urlpatterns = [
    path('recherche', SearchResultsView, name='search_cards'),

    path('fiches-de-maintiens-serpents/', SnakeListView.as_view(), name="snake_list"),
    path('fiches-de-maintiens-serpents/ajouter/', SnakeFormView.as_view(), name="snake_create"),
    path('fiches-de-maintiens-serpents/<slug:slug>/', SnakeDetailView.as_view(), name='snake_details'),

    path('fiches-de-maintiens-amphibiens/', AmphibianListView.as_view(), name="amphibian_list"),
    path('fiches-de-maintiens-amphibiens/ajouter/', AmphibianFormView.as_view(), name="amphibian_create"),
    path('fiches-de-maintiens-amphibiens/<slug:slug>/', AmphibianDetailView.as_view(), name="amphibian_details"),

    path('fiches-de-maintiens-lezards/', LizardListView.as_view(), name="lizard_list"),
    path('fiches-de-maintiens-lezards/ajouter/', LizardFormView.as_view(), name="lizard_create"),
    path('fiches-de-maintiens-lezards/<slug:slug>/', LizardDetailView.as_view(), name="lizard_details"),

    path('communaute/<int:pk>', CommunityDetailView.as_view(), name="community_detail"),
    path('communaute/', CommunityListView.as_view(), name="community_list"),

    path('petites-annonces/', AdsListView.as_view(), name="ads_list"),
    path('petites-annonces/filtrer/', SearchAdsResultsView, name="ads_filter"),
    path('petites-annonces/ajouter/', AdsCreateView.as_view(), name="ads_create"),
    path('petites-annonces/mes-annonces/', AdsOwnListView.as_view(), name="ads_own_list"),
    path('petites-annonces/<int:pk>/supprimer/', AdsDeleteView.as_view(), name="ads_delete"),
    path('petites-annonces/<int:pk>', AdsDetailsView.as_view(), name="ads_details"),
    path('petites-annonces/<int:pk>/update/', AdsUpdateView.as_view(), name="ads_update"),

    path('suggestions/<int:pk>', SuggestionDetailView.as_view(), name="suggestion_details"),
    path('suggestions/ajouter/', SuggestionCreateView.as_view(), name="suggestion_create"),
    path('suggestions/', SuggestionListView.as_view(), name="suggestion_list"),

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
