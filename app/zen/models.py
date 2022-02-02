from django.db import models


class ZenArticle(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    link = models.URLField(verbose_name='Source link', unique=True)
    likes = models.IntegerField()
    reads = models.IntegerField()
    comments = models.IntegerField()
    to_parse_interval = models.IntegerField()
    public_datetime = models.IntegerField()
    length = models.IntegerField()
    num_images = models.IntegerField()
    audience = models.IntegerField()
    visitors = models.IntegerField()
    read_time = models.IntegerField()
    subscribers = models.IntegerField()

    class Meta:
        verbose_name = "Article"
        db_table = 'zen_articles'


class ZenFeed(models.Model):
    article = models.ForeignKey(ZenArticle, on_delete=models.CASCADE, related_name='feeds')

    name = models.CharField(verbose_name='Name', max_length=25)
    users_num = models.IntegerField(verbose_name='Users')

    class Meta:
        verbose_name = "Feed"
        db_table = 'zen_feeds'

