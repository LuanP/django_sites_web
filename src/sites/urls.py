from django.urls import path

from .views import SiteListView, SiteDetailView


urlpatterns = [
    path('', SiteListView.as_view(), name='home_list'),
    path('sites', SiteListView.as_view(), name='list'),
    path('sites/<int:id>/', SiteDetailView.as_view(), name='detail'),
    path('summary', SiteListView.as_view(), name='summary')
]
