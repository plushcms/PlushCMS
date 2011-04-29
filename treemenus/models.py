# -*- coding: utf-8 -*-

from itertools import chain

from django.db import models
from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext as _

class MenuItem(models.Model):
    parent = models.ForeignKey("self", verbose_name = ugettext_lazy("Parent"), null = True, blank = True)
    caption = models.CharField(ugettext_lazy("Name"), max_length = 50, help_text = "Enter a name which doesn't exceed 50 characters.")
    url = models.CharField(ugettext_lazy("Address"), max_length = 200, blank = False, help_text = "Enter the correct web address.")
    level = models.IntegerField(ugettext_lazy("Level"), default = 0, editable = False)
    rank = models.IntegerField(ugettext_lazy("Rank"), default = 0, editable = False)
    menu = models.ForeignKey("Menu", related_name = "contained_items", verbose_name = ugettext_lazy("Menu"), null = True, blank = True, editable = False)

    def __unicode__(self):
        return self.caption

    def save(self, force_insert = False, **kwargs):
        from plushcms.treemenus.utils import clean_ranks

        old_level = self.level

        if self.parent:
            self.level = self.parent.level + 1

        else:
            self.level = 0

        if self.pk:
            new_parent = self.parent
            old_parent = MenuItem.objects.get(pk = self.pk).parent

            if old_parent != new_parent:
                if new_parent:
                    clean_ranks(new_parent.children())
                    self.rank = new_parent.children().count()

                super(MenuItem, self).save(force_insert, **kwargs)

                if old_parent:
                    clean_ranks(old_parent.children())

            else:
                super(MenuItem, self).save(force_insert, **kwargs)

        else:
            if not self.has_siblings():
                self.rank = 0

            else:
                siblings = self.siblings().order_by("-rank")
                self.rank = siblings[0].rank + 1

            super(MenuItem, self).save(force_insert, **kwargs)

        if old_level != self.level:
            for child in self.children():
                child.save()

    def delete(self):
        from plushcms.treemenus.utils import clean_ranks

        old_parent = self.parent
        super(MenuItem, self).delete()

        if old_parent:
            clean_ranks(old_parent.children())

    def caption_with_spacer(self):
        spacer = ""

        for x in xrange(0, self.level):
            spacer = spacer + u"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

        if self.level > 0:
            spacer = spacer + u"|-&nbsp;"

        return spacer + self.caption

    def get_flattened(self):
        flat_structure = [self]

        for child in self.children():
            flat_structure = chain(flat_structure, child.get_flattened())

        return flat_structure

    def siblings(self):
        if not self.parent:
            return MenuItem.objects.none()

        else:
            if not self.pk:
                return self.parent.children()

            else:
                return self.parent.children().exclude(pk = self.pk)

    def hasSiblings(self):
        import warnings

        warnings.warn("hasSiblings() is deprecated, use has_siblings() instead.", DeprecationWarning, stacklevel = 2)

        return self.has_siblings()

    def has_siblings(self):
        return self.siblings().count() > 0

    def children(self):
        _children = MenuItem.objects.filter(parent = self).order_by("rank",)

        for child in _children:
            child.parent = self

        return _children

    def hasChildren(self):
        import warnings

        warnings.warn("hasChildren() is deprecated, use has_children() instead.", DeprecationWarning, stacklevel = 2)

        return self.has_children()

    def has_children(self):
        return self.children().count() > 0

class Menu(models.Model):
    name = models.CharField(ugettext_lazy("Name"), max_length = 50, help_text = "Enter a name which doesn't exceed 50 characters.", unique = True)
    root_item = models.ForeignKey(MenuItem, related_name = "is_root_item_of", verbose_name = ugettext_lazy("Root Item"), null = True, blank = True, editable = False)

    def save(self, force_insert = False, **kwargs):
        if not self.root_item:
            root_item = MenuItem()
            root_item.caption = _("Root")

            if not self.pk:
                super(Menu, self).save(force_insert, **kwargs)
                force_insert = False

            root_item.menu = self
            root_item.save()
            self.root_item = root_item

        super(Menu, self).save(force_insert, **kwargs)

    def delete(self):
        if self.root_item is not None:
            self.root_item.delete()

        super(Menu, self).delete()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")
