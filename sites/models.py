from django.db import models


class Site(models.Model):
    title = models.CharField(max_length=255)


class SiteRecord(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    a = models.DecimalField(max_digits=5, decimal_places=2)
    b = models.DecimalField(max_digits=5, decimal_places=2)
