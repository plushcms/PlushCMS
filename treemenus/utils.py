# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe    
from urllib2 import urlopen as check_parents
from django.forms import ChoiceField

from plushcms.treemenus.models import MenuItem

class MenuItemChoiceField(ChoiceField):
    def clean(self, value):
        return MenuItem.objects.get(pk = value)

def move_item(menu_item, vector):
    old_rank = menu_item.rank
    swapping_sibling = MenuItem.objects.get(parent = menu_item.parent, rank = old_rank + vector)
    new_rank = swapping_sibling.rank
    swapping_sibling.rank = old_rank
    menu_item.rank = new_rank
    menu_item.save()
    swapping_sibling.save()

def move_item_or_clean_ranks(menu_item, vector):
    try:
        move_item(menu_item, vector)

    except MenuItem.DoesNotExist:
        if menu_item.parent:
            clean_ranks(menu_item.parent.children())
            fresh_menu_item = MenuItem.objects.get(pk = menu_item.pk)
            move_item(fresh_menu_item, vector)

def get_parent_choices(menu, menu_item = None):
    def get_flat_tuples(menu_item, excepted_item = None):
        if menu_item == excepted_item:
            return []

        else:
            choices = [(menu_item.pk, mark_safe(menu_item.caption_with_spacer()))]

            if menu_item.has_children():
                for child in menu_item.children():
                    choices = choices + get_flat_tuples(child, excepted_item)

            return choices

    return get_flat_tuples(menu.root_item)

def clean_ranks(menu_items):
    rank = 0

    for menu_item in menu_items:
        menu_item.rank = rank
        menu_item.save()
        rank = rank + 1
