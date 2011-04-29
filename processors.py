#-*- coding: utf-8 -*-

from plushcms.core.models import News
from plushcms.core.models import NewsCategory
from plushcms.core.models import Links
from plushcms.core.models import Partners
from plushcms.core.forms import SearchForm

from sys import version
from django import get_version
from settings import PLUSH_VERSION
from settings import UPDATE_DATE

def showTopNews(request):
    part = 5
    topNews = News.objects.all().filter(isHeadline = True).filter(isDraft = False)[:part]

    return {"topNews" : topNews, "partOfTopNews" : topNews.count()}

def showCategories(request):
    return {"categories" : NewsCategory.objects.all(), "numberOfCategories" : NewsCategory.objects.count()}

def showLinks(request):
    return {"links" : Links.objects.all(), "numberOfLinks" : Links.objects.count()}

def showPartners(request):
    return {"partners" : Partners.objects.all(), "numberOfPartners" : Partners.objects.count()}

def showSearchForm(request):
    return {"search" : SearchForm()}

def showSystemDetails(request):
    pythonVersion = version.split()[0]
    djangoVersion = get_version()
    plushcmsVersion = PLUSH_VERSION
    update = UPDATE_DATE

    return {"pythonVersion" : pythonVersion, "djangoVersion" : djangoVersion, "plushcmsVersion": plushcmsVersion, "update" : update}
