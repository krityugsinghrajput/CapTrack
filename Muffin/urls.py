from django.urls import path
from Muffin.views import SearchView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
]


