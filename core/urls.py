# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin

from plushcms.core.views import showPartOfNews
from plushcms.core.views import showCategories
from plushcms.core.views import showNewsByTitle
from plushcms.core.views import showSubpage
from plushcms.core.views import showSearchResults
from plushcms.core.views import showContactSuccessfully
from plushcms.core.views import showContactUnsuccessfully
from plushcms.core.views import showPhotosOrFiles
from plushcms.core.views import captchaGenerator

from plushcms.core.feeds import RSS

admin.autodiscover()

urlpatterns = patterns("",
    url(r"^$", showPartOfNews),
    url(r"^(?P<newsTitle>.*)\.html$", showNewsByTitle),
    url(r"^site/(?P<pageNumber>[\w\-_]+)/$", showPartOfNews),
    url(r"^subpage/contact/info/$", showContactSuccessfully),
    url(r"^subpage/contact/info-error/$", showContactUnsuccessfully),
    url(r"^subpage/(?P<subpage>[\w\-_]+)/$", showSubpage),
    url(r"^subpage/(?P<url>[\w\-_]+)/(?P<title>[\w\-_]+)/$", showPhotosOrFiles),
    url(r"^category/(?P<categoryName>[\w\-_]+)/(?P<pageNumber>[\w\-_]+)/$", showCategories),
    url(r"^category/(?P<categoryName>[\w\-_]+)/$", showCategories),
    url(r"^search/(?P<pageNumber>[\w\-_]+)/$", showSearchResults),
    url(r"^captcha.png/(?P<url>[\w\-_]+)$", captchaGenerator),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^feeds/rss/$", RSS(), name = "feeds_rss")
)
