# -*- coding: utf-8 -*-

from plushcms.core.models import News

from django.contrib.syndication.views import Feed

class RSS(Feed):
    title = "PlushCMS v0.1.1"
    link = "/"
    description = "PlushCMS v0.1.1 - CMS system written in Python and Django"

    def items(self):
        numberOfNews = 10

        return News.objects.all().filter(isDraft = False)[:numberOfNews]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.datetime

    def item_description(self, item):
        return item.text
