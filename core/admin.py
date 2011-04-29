# -*- coding: utf-8 -*-

from django.contrib import admin

from plushcms.core.models import NewsCategory
from plushcms.core.models import Links
from plushcms.core.models import News
from plushcms.core.models import Comments
from plushcms.core.models import Subpage
from plushcms.core.models import Partners

# That action will no longer be available site-wid
admin.site.disable_action("delete_selected")

class NewsCategory_Admin(admin.ModelAdmin):
    list_display = ("showIcon", "title")
    actions = ["delete_selected"]

class Links_Admin(admin.ModelAdmin):
    list_display = ("title",)
    actions = ["delete_selected"]

class News_Admin(admin.ModelAdmin):
    list_display = ("title", "author", "isHeadline", "isDraft", "datetime")
    list_filter = ["category", "author"]
    actions = ["delete_selected"]

    # Sets the author's news
    def save_model(self, request, obj, form, change):
        if getattr(obj, "author", None) is None:
            obj.author = request.user

        obj.save()

    # Loading TinyMCE
    class Media:
        js = ("/img/js/tiny_mce/tiny_mce.js", "/img/js/textareas.js")

class Comments_Admin(admin.ModelAdmin):
    list_display = ("nick", "news", "datetime")
    actions = ["delete_selected"]

    # Loading TinyMCE
    class Media:
        js = ("/img/js/tiny_mce/tiny_mce.js", "/img/js/textareas.js")

class Subpage_Admin(admin.ModelAdmin):
    list_display = ("mod", "title",)
    actions = ["delete_selected"]

    # Loading TinyMCE
    class Media:
        js = ("/img/js/tiny_mce/tiny_mce.js", "/img/js/textareas.js")

class Partners_Admin(admin.ModelAdmin):
    list_display = ("title",)
    actions = ["delete_selected"]

admin.site.register(NewsCategory, NewsCategory_Admin)
admin.site.register(Links, Links_Admin)
admin.site.register(News, News_Admin)
admin.site.register(Comments, Comments_Admin)
admin.site.register(Subpage, Subpage_Admin)
admin.site.register(Partners, Partners_Admin)
