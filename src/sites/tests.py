from django.urls import reverse
from django.test import TestCase, Client


class TestSite(TestCase):
    fixtures = ['sites.json']

    def setUp(self):
        self.client = Client()

    def test_home_site_list(self):
        response = self.client.get(reverse('sites:home_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/list.html')

    def test_response(self):
        response = self.client.get(reverse('sites:list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/list.html')

    def test_site_detail_not_found(self):
        response = self.client.get(reverse('sites:detail', kwargs={'id': 9999}))

        self.assertEqual(response.status_code, 404)

    def test_site_detail(self):
        response = self.client.get(reverse('sites:detail', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/detail.html')

    def test_summary(self):
        response = self.client.get(reverse('sites:summary_sum'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/summary.html')

    def test_summary_average(self):
        response = self.client.get(reverse('sites:summary_average'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites/summary.html')

    def test_sites_list_nav_is_active(self):
        response = self.client.get(reverse('sites:list'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item active">\n        <a class="nav-link" href="/sites">Sites</a>',
            html
        )

    def test_sites_list_nav_is_active_in_site_detail(self):
        response = self.client.get(reverse('sites:detail', kwargs={'id': 1}))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item active">\n        <a class="nav-link" href="/sites">Sites</a>',
            html
        )

    def test_sites_list_nav_is_not_active_in_summary_sum(self):
        response = self.client.get(reverse('sites:summary_sum'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item">\n        <a class="nav-link" href="/sites">Sites</a>',
            html
        )

    def test_sites_list_nav_is_not_active_in_summary_average(self):
        response = self.client.get(reverse('sites:summary_average'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item">\n        <a class="nav-link" href="/sites">Sites</a>',
            html
        )

    def test_sites_summary_sum_nav_is_active(self):
        response = self.client.get(reverse('sites:summary_sum'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item active">\n        <a class="nav-link" href="/summary">Summary</a>',
            html
        )

    def test_sites_summary_average_nav_is_active(self):
        response = self.client.get(reverse('sites:summary_average'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<li class="nav-item active">\n        <a class="nav-link" href="/summary">Summary</a>',
            html
        )

    def test_summary_sum_active_link(self):
        response = self.client.get(reverse('sites:summary_sum'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<a href="/summary"><button type="button" class="btn btn-primary active">Sum</button></a',
            html
        )

    def test_summary_sum_average_is_not_active_link(self):
        response = self.client.get(reverse('sites:summary_sum'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<a href="/summary-average"><button type="button" class="btn btn-primary">Average</button></a',
            html
        )

    def test_summary_average_active_link(self):
        response = self.client.get(reverse('sites:summary_average'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<a href="/summary-average"><button type="button" class="btn btn-primary active">Average</button></a',
            html
        )

    def test_summary_average_sum_is_not_active_link(self):
        response = self.client.get(reverse('sites:summary_average'))
        html = response.content.decode('utf8')

        self.assertIn(
            '<a href="/summary"><button type="button" class="btn btn-primary">Sum</button></a',
            html
        )
