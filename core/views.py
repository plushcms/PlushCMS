# -*- coding: utf-8 -*-

import hashlib

from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime

from plushcms.core.models import News
from plushcms.core.models import NewsCategory
from plushcms.core.models import Comments
from plushcms.core.models import Subpage

from plushcms.core.forms import ContactForm
from plushcms.core.forms import CommentsForm

from plushcms.gallery.models import Albums
from plushcms.gallery.models import Photos

from plushcms.storage.models import Directories
from plushcms.storage.models import Files

from plushcms.plushlib import sendEmail
from plushcms.plushlib import renderCapchaImage

from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage

# Function for more effective concatenating the QuerySets
from itertools import chain

# Imports used by the Contact form
from settings import SERVER
from settings import PORT
from settings import LOGIN
from settings import PASSWORD
from settings import SENDER
from settings import RECIPIENT

def showPartOfNews(request, pageNumber = "1"):
    """Returns a specified part of news based on the 'pageNumber'.
       part - specifies the number of news on page"""
    part = 5
    paginator = Paginator(News.objects.all().filter(isDraft = False), part)

    try:
        posts = paginator.page(int(pageNumber))

    except (EmptyPage, InvalidPage, ValueError):
        return HttpResponseRedirect("/site/1/")

    return render_to_response("index.html", {"posts" : posts}, context_instance = RequestContext(request))

def showCategories(request, categoryName, pageNumber = "1"):
    """Returns a specified part of news from the "categoryName" based on the 'pageNumber'.
       part - specifies the number of news on page"""
    part = 5
    category = NewsCategory.objects.get(url = categoryName)
    paginator = Paginator(category.news_set.all().filter(isDraft = False), part)

    try:
        posts = paginator.page(int(pageNumber))

    except (EmptyPage, InvalidPage, ValueError):
        return HttpResponseRedirect("/category/%s/1/" % categoryName)

    return render_to_response("category.html", {"category" : category, "posts" : posts}, context_instance = RequestContext(request))

def showNewsByTitle(request, newsTitle):
    """Returns single news with all of category based on the 'newsTitle'"""
    news = News.objects.get(url = u"%s.html" % newsTitle)

    if request.POST:
        data = request.POST.copy()
        data["news"] = news.id
        data["datetime"] = datetime.now()
        form = CommentsForm(data)

        if form.is_valid():
            if hashlib.sha1(request.POST["token"]).hexdigest() == request.session["token_news_%s" % news.id]:
                form.save()

            else:
                del data["token"]
                form = CommentsForm(data)

                return render_to_response("news.html", {"news" : news, "form" : form, "tokenValid" : "0"}, context_instance = RequestContext(request))

            return HttpResponseRedirect(u"%s.html" % newsTitle)

    else:
        form = CommentsForm()

    return render_to_response("news.html", {"news" : news, "form" : form, "error" : form._get_errors(), "tokenValid" : "1"}, context_instance = RequestContext(request))

def showSubpage(request, subpage):
    """Return subpage"""
    site = Subpage.objects.get(url = subpage)

    # Collection of albums and photos
    combo = {}
    # Collection of directories and files
    directories = []

    if request.POST:
        data = request.POST.copy()
        form = ContactForm(data)

        if form.is_valid():
            if hashlib.sha1(form.cleaned_data["token"]).hexdigest() == request.session["token_subpage_%s" % site.id]:
                nick = form.cleaned_data["nick"]
                email = form.cleaned_data["email"]
                topic = form.cleaned_data["topic"]
                message = form.cleaned_data["message"]
                message = message.replace("\n", "<br />")

                try:
                    sendEmail(SERVER, PORT, LOGIN, PASSWORD, "PlushCMS v0.1.1 <%s>" % SENDER, RECIPIENT, "PlushCMS v0.1.1 - Contact form", "<b>Topic:</b> %s<br /><br /><b>Nick:</b> %s<br /><b>E-mail:</b> %s<br /><br /><b>%s:</b> <br />%s" % (topic, nick, email, "Message".decode("utf-8"), message))

                    return HttpResponseRedirect("/subpage/contact/info/")

                except:
                    return HttpResponseRedirect("/subpage/contact/info-error/")

            else:
                valid = 2

                if data["token"]: 
                    valid = 1     

                del data["token"]
                form = ContactForm(data)

                return render_to_response("subpage.html", {"site" : site, "form" : form, "combo" : combo, "tokenValid" : str(valid)}, context_instance = RequestContext(request))

        else:
            valid = 1

            if not data["token"]:
                valid = 2

                if hashlib.sha1(request.POST["token"]).hexdigest() == request.session["token_subpage_%s" % site.id]:
                    valid = 0

            del data["token"]
            form = ContactForm(data)

            return render_to_response("subpage.html", {"site" : site, "form" : form, "combo" : combo, "tokenValid" : str(valid)}, context_instance = RequestContext(request))

    else:
        form = ContactForm()

    # Gallery module
    if site.selectedModule == 1:
        albums = Albums.objects.all().filter(selectedModule = 0)

        for x, y in enumerate(albums):
            try:
                combo[y] = Photos.objects.filter(selectedModule = 0).filter(parent = y)[0].photoMin

            except:
                combo[y] = 0

    # Storage module
    if site.selectedModule == 2:
        directories = Directories.objects.all().filter(selectedModule = 0)
        directories = [(x, Files.objects.filter(selectedModule = 0).filter(parent = x).count()) for x in directories]

    return render_to_response("subpage.html", {"site" : site, "form" : form, "combo" : combo, "tokenValid" : "0", "directories" : directories}, context_instance = RequestContext(request))

def showPhotosOrFiles(request, url, title):
    """Returns all photos from the album or files from the directory based on the 'title'"""
    site = Subpage.objects.get(url = url)

    if site.selectedModule == 1:
        album = Albums.objects.get(directory = title)
        photos = Photos.objects.filter(parent = album).filter(selectedModule = 0)

        return render_to_response("subpage.html", {"site" : site, "photos" : photos, "album" : album.title}, context_instance = RequestContext(request))

    if site.selectedModule == 2:
        director = Directories.objects.get(directory = title)
        files = Files.objects.filter(parent = director).filter(selectedModule = 0)

        return render_to_response("subpage.html", {"site" : site, "files" : files, "directory" : director.title}, context_instance = RequestContext(request))

def showSearchResults(request, pageNumber = "1"):
    """Returns a searching results (comparison with title and the content of news and subpage) based on the 'pageNumber'.
       part - specifies the number of results on page"""
    if request.GET.get("phrase", u"").strip():
        phrase = request.GET.get("phrase", u"").strip()[:30]

        part = 5
        paginator = Paginator(list(chain((News.objects.filter(title__contains = phrase) | News.objects.filter(text__contains = phrase)).filter(isDraft = False), Subpage.objects.filter(title__contains = phrase) | Subpage.objects.filter(text__contains = phrase))), part)

        try:
            posts = paginator.page(int(pageNumber))

        except (EmptyPage, InvalidPage, ValueError):
            return HttpResponseRedirect("/search/1/?phrase=") 

    else:
        posts = []
        phrase = ""

    return render_to_response("search.html", {"phrase" : phrase, "posts" : posts}, context_instance = RequestContext(request))

def captchaGenerator(request, url):
    """Returns captcha image"""
    captcha = renderCapchaImage(170, 50, 8, 24)

    response = HttpResponse()
    response["Content-Type"] = "image/png"
    response.write(captcha["picture"])

    request.session["token_%s" % url] = captcha["imghash"]

    return response

def showContactSuccessfully(request):
    """Returns positive information about sending e-mail"""
    return render_to_response("contactInfoOk.html", context_instance = RequestContext(request))

def showContactUnsuccessfully(request):
    """returns negative information about sending e-mail"""
    return render_to_response("contactInfoError.html", context_instance = RequestContext(request))

def error500(request):
    """Server error view"""
    return render_to_response("subpage.html", {"error" : "500"}, context_instance = RequestContext(request))

def error404(request):
    """Page not found view"""
    return render_to_response("subpage.html", {"error" : "404"}, context_instance = RequestContext(request))
