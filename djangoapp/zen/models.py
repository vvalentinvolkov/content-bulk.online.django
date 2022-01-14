from django.db import models


class ZenArticle(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    link = models.URLField(verbose_name='Source link', unique=True)

    class Meta:
        verbose_name = "Article"
        db_table = 'zen_article'


class ZenFeed(models.Model):
    article = models.ForeignKey(ZenArticle, on_delete=models.CASCADE, related_name='feeds')

    name = models.CharField(verbose_name='Name', max_length=25)
    users_num = models.IntegerField(verbose_name='Users')

    class Meta:
        verbose_name = "Feed"

