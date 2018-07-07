from django.urls import path

from .views import SiteListView

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


urlpatterns = [
    path('', SiteListView.as_view(), name='home_list'),
    path('sites', SiteListView.as_view(), name='site_list')
]
