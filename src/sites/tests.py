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
