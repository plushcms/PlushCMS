# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

import re
from django.core.exceptions import ValidationError

from plushcms.settings import MEDIA_ROOT

from plushcms.plushlib import scaleImage
from plushcms.plushlib import highlightCode

def validateSigns(value):
    """Nick field validation from comment form"""
    pattern = re.compile(r"^[\wĄĆĘŁŃÓŚŹŻąćęłńóśźż]+$", re.U)

    if not re.match(pattern, value):
        raise ValidationError("Invalid value.")

def validateSpace(value):
    """Checking white-spaces in the form fields"""
    if not value.strip():
        raise ValidationError("Invalid value.")

class NewsCategory(models.Model):
    """Category model for News"""
    title = models.CharField(max_length = 150, verbose_name = "Name", unique = True, help_text = "Enter a name which doesn't exceed 150 characters.")
    url = models.SlugField(max_length = 150, verbose_name = "Address", editable = False)
    icon = models.ImageField(upload_to = "icons", verbose_name = "Icon", blank = False, help_text = "Only image uploads are allowed.")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def showIcon(self):
        return "<img src=\"/img/%s\" \>" % self.icon

    showIcon.allow_tags = True
    showIcon.short_description = "Icon"

    def save(self, force_insert = False, force_update = False):
        """Generate the url from the category name"""
        self.url = slugify(unicode(self.title.replace(u"ł", "l").replace(u"Ł", "L")))
        super(NewsCategory, self).save(force_insert, force_update)
        scaleImage(self.icon.path, width = 13)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

class News(models.Model):
    """News model"""
    category = models.ManyToManyField(NewsCategory, verbose_name = "Categories")
    title = models.CharField(max_length = 150, verbose_name = "Title", help_text = "Enter a title which doesn't exceed 150 characters.")
    text = models.TextField(verbose_name = "Text")
    datetime = models.DateTimeField(verbose_name = "Publication date")
    isDraft = models.BooleanField(verbose_name = "Working copy flag")
    isHeadline = models.BooleanField(verbose_name = "Show on \"Top news\"")
    author = models.ForeignKey(User, verbose_name = "Author", null = True, blank = True, editable = False)
    url = models.SlugField(max_length = 150, editable = False)

    # It is used by search engine to listing results
    verbose_name = "News"

    def save(self, force_insert = False, force_update = False):
        self.url = u"%s.html" % slugify(unicode(self.title.replace(u"ł", "l").replace(u"Ł", "L")))
        self.text = highlightCode(self.text)
        super(News, self).save(force_insert, force_update)

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "news"
        verbose_name_plural = "news"

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

    def get_absolute_url(self):
        return unicode("/%s" % self.url)

class Links(models.Model):
    """Links model"""
    title = models.CharField(max_length = 150, verbose_name = "Name", unique = True, help_text = "Enter a name which doesn't exceed 150 characters.")
    url = models.URLField(max_length = 150, verbose_name = "Address", unique = True, help_text = "Enter the correct web address.")

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

class Comments(models.Model):
    """Comments model for News"""
    nick = models.CharField(max_length = 150, verbose_name = "Nick", validators = [validateSigns], help_text = "Enter a nick which doesn't exceed 150 characters.")
    www = models.URLField(max_length = 150, verbose_name = "Address", blank = True, null = True, help_text = "Enter the correct web address.")
    news = models.ForeignKey(News, verbose_name = "News", help_text = "Choose the news.")
    text = models.TextField(max_length = 200, verbose_name = "Text", validators = [validateSpace])
    datetime = models.DateTimeField(verbose_name = "Publication date")

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return str(self.news)

    def __unicode__(self):
        return unicode(self.news)

class Subpage(models.Model):
    """Subpage model"""
    title = models.CharField(max_length = 150, verbose_name = "Name", unique = True, help_text = "Enter a name which doesn't exceed 150 characters.")
    text = models.TextField(verbose_name = "Text")
    url = models.CharField(max_length = 150, verbose_name = "Address", unique = True, editable = False)
    modules = ((-1, "Standard subpage"), (0, "Contact form"), (1, "Gallery module"), (2, "Storage module"))
    selectedModule = models.IntegerField(max_length = 150, verbose_name = "Module", choices = modules, default = -1, blank = False, null = False, help_text = "Choose the module.")

    # It is used by search engine to listing results
    verbose_name = u"Subpage"

    def mod(self):
        if self.selectedModule == -1:
            return self.modules[0][1]
        elif self.selectedModule == 0:
            return self.modules[1][1]
        elif self.selectedModule == 1:
            return self.modules[2][1]
        else:
            return self.modules[3][1]

    mod.allow_tags = True
    mod.short_description = "Selected module"

    class Meta:
        verbose_name = u"subpage"
        verbose_name_plural = u"subpages"

    def save(self, force_insert = False, force_update = False):
        """Generate the url from the title"""
        self.url = slugify(unicode(self.title.replace(u"ł", "l").replace(u"Ł", "L")))
        super(Subpage, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

class Partners(models.Model):
    """Partners model"""
    title = models.CharField(max_length = 150, verbose_name = "Name", unique = True, help_text = "Enter a name which doesn't exceed 150 characters.")
    url = models.URLField(max_length = 150, verbose_name = "Address", unique = True, help_text = "Enter the correct web address.")
    logo = models.ImageField(upload_to = "partners", verbose_name = "Logo", help_text = "Only image uploads are allowed.")

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"

    def save(self, force_insert = False, force_update = False):
        """Scale logo image"""
        super(Partners, self).save(force_insert, force_update)
        # Default width is 200px
        scaleImage(self.logo.path)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)
