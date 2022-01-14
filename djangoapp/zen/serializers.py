from rest_framework import serializers

from .models import ZenArticle, ZenFeed


class ZenFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZenFeed
        exclude = ['article']

    def create(self, validated_data):
        return ZenFeed.objects.create(**validated_data)


class ZenArticleSerializer(serializers.ModelSerializer):
    feeds = ZenFeedSerializer(many=True)

    class Meta:
        model = ZenArticle
        fields = '__all__'

    def create(self, validated_data):
        feeds_data = validated_data.pop('feeds')
        article = ZenArticle.objects.create(**validated_data)
        for feed_data in feeds_data:
            ZenFeed.objects.create(article=article, **feed_data)
        return article
