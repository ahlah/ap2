from django.urls import path

from .views import IndexView, SearchView

urlpatterns = [
    path('', IndexView.as_view()),
    path('search/', SearchView.as_view()),
]