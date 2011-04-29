# -*- coding: utf-8 -*-

from django import template
from django.template.defaulttags import url
from django.template.defaulttags import URLNode
from django.template import Node

from plushcms.treemenus.models import Menu
from plushcms.treemenus.models import MenuItem
from plushcms.treemenus.config import APP_LABEL

from django.template import TOKEN_BLOCK
from django.template import Token

register = template.Library()

# 16.02.2011 - dodany try except
def show_menu(context, menu_name, menu_type = None):
    try:
        menu = Menu.objects.get(name = menu_name)
    except:
        return None
    else:
        context["menu"] = menu

        if menu_type:
            context["menu_type"] = menu_type

        return context

register.inclusion_tag("%s/menu.html" % APP_LABEL, takes_context = True)(show_menu)

def show_menu_item(context, menu_item):
    if not isinstance(menu_item, MenuItem):
        raise template.TemplateSyntaxError, "Podany argument musi być obiektem MenuItem."

    context["menu_item"] = menu_item

    return context

register.inclusion_tag("%s/menu_item.html" % APP_LABEL, takes_context = True)(show_menu_item)
# 06.03.2011 - usunięto ReverseNamedURLNode, reverse_named_ulr i jego rejestracja
