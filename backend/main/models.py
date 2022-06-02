from django.db import models

class TestModel(models.Model):
    name = models.CharField(default='', max_length=10)
    test = models.IntegerField(default=5)