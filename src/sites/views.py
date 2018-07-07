from django.views import generic

from .models import Site


class SiteListView(generic.ListView):
    template_name = 'sites/list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all()


class SiteDetailView(generic.DetailView):
    model = Site
    template_name = 'sites/detail.html'
    context_object_name = 'site'
    pk_url_kwarg = 'id'
