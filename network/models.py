from django.db import models
# Create your models here.


class Reaction(models.Model):
    # widget = models.ImageField
    reaction_type = models.CharField(max_length=20)
    weight = models.IntegerField()


class Post(models.Model):
    author = models.ForeignKey('account.Profile', on_delete=models.CASCADE)
    date = models.DateTimeField('Data e Hora da Postagem', 'DateTimeStamp')
    text = models.TextField('Postagem')
