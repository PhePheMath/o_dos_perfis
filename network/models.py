from django.db import models
# Create your models here.


class Reaction(models.Model):
    # widget = models.ImageField
    reaction_type = models.CharField(max_length=20)
    weight = models.IntegerField()


