from django.db import models

class CEB(models.Model):
    username = models.CharField(max_length=20)
    amount = models.JSONField()
    units = models.JSONField()
    dues_amount = models.FloatField()
    payments = models.JSONField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class NWSDB(models.Model):
    username = models.CharField(max_length=20)
    amount = models.JSONField()
    units = models.JSONField()
    dues_amount = models.FloatField()
    payments = models.JSONField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
