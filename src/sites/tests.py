from django.urls import reverse
from django.test import TestCase, Client


class TestSite(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_site_list(self):
        sites_list = self.client.get(reverse('sites:home_list'))

        self.assertTrue(sites_list.status_code, 200)
        self.assertTemplateUsed(sites_list, 'sites/list.html')

    def test_sites_list(self):
        sites_list = self.client.get(reverse('sites:list'))

        self.assertTrue(sites_list.status_code, 200)
        self.assertTemplateUsed(sites_list, 'sites/list.html')

    def test_site_not_found(self):
        sites_list = self.client.get(reverse('sites:detail', kwargs={'id': 9999}))

        self.assertTrue(sites_list.status_code, 404)
