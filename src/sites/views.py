from django.db.models import Sum
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


class SiteSummarySumTemplateView(generic.TemplateView):
    template_name = 'sites/summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sites'] = Site.objects.all().annotate(
            result_a=Sum('siterecord__a'),
            result_b=Sum('siterecord__b')
        )

        return context


class SiteSummaryAverageTemplateView(generic.TemplateView):
    template_name = 'sites/summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['sites'] = Site.objects.all().annotate(
        #     result_a=Avg('siterecord__a'),
        #     result_b=Avg('siterecord__b')
        # )
        context['sites'] = Site.objects.raw('''
            SELECT "sites_site"."id",
                   "sites_site"."title",
                   AVG("sites_siterecord"."a") AS "result_a",
                   AVG("sites_siterecord"."b") AS "result_b"
            FROM "sites_site"
            LEFT OUTER JOIN "sites_siterecord" ON
                ("sites_site"."id" = "sites_siterecord"."site_id")
            GROUP BY "sites_site"."id"
        ''')

        return context
