from django.views import generic

from .models import Site


class SiteListView(generic.ListView):
    template_name = 'sites/list.html'

    def get_queryset(self):
        return Site.objects.all()
