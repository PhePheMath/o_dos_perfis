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


class React(models.Model):
    profile = models.ForeignKey('account.Profile', on_delete=models.CASCADE,
                                related_name='all_reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='reactions')
    date = models.DateTimeField('Data e Hora da Postagem', 'DateTimeStamp')
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE,
                                 related_name='where')


class Comment(models.Model):
    text = models.TextField('Comment')
    date = models.DateTimeField('Data e Hora da Postagem', 'DateTimeStamp')
    profile = models.ForeignKey('account.Profile', on_delete=models.CASCADE,
                                related_name='someone')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='on')
