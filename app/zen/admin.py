from django.contrib import admin

from .models import ZenArticle, ZenFeed


@admin.register(ZenArticle)
class ZenArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ZenFeed)
class ZenArticleAdmin(admin.ModelAdmin):
    pass
