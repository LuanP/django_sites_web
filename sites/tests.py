from django.test import TestCase, Client


class TestSite(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sites_list(self):
        sites_list = self.client.get('/')

        self.assertTrue(sites_list.status_code, 200)
        self.assertTemplateUsed(sites_list, 'sites/list.html')
