# -*- coding: utf-8 -*-

from django import forms

from plushcms.core.models import Comments

class SearchForm(forms.Form):
    """Search form field"""
    phrase = forms.CharField(widget = forms.TextInput(attrs = {"class" : "search"}))

    def __str__(self):
        return str(self.phrase)

    def __unicode__(self):
        return unicode(self.phrase)

class ContactForm(forms.Form):
    """Contact form field"""
    nick = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {"class" : "search"}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {"class" : "search"}))
    topic = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {"class" : "search"}))
    message = forms.CharField(widget = forms.Textarea(attrs = {"class" : "textarea"}))
    token = forms.CharField(max_length = 8, widget = forms.TextInput(attrs = {"class" : "search"}))

class CommentsForm(forms.ModelForm):
    """Comments form field"""
    token = forms.CharField(max_length = 8, widget = forms.TextInput(attrs = {"class" : "search"}))

    class Meta:
        model = Comments
        widgets = {"nick" : forms.TextInput(attrs = {"class" : "search"}),
                   "www" : forms.TextInput(attrs = {"class" : "search"}),
                   "text" : forms.Textarea(attrs = {"class" : "textarea"})}
