# -*- coding: utf-8 -*-

from django.contrib import admin

from plushcms.gallery.models import Albums
from plushcms.gallery.models import Photos

from plushcms.gallery.gallerylib import deleteSelectedAlbums
from plushcms.gallery.gallerylib import deleteSelectedPhotos

class Albums_Admin(admin.ModelAdmin):
    list_display = ("title", "mod")
    list_filter = ["selectedModule",]
    actions = [deleteSelectedAlbums]

class Photos_Admin(admin.ModelAdmin):
    list_display = ("parent", "showAlbumAccessModifiers", "showPhotoName", "showPhotoAccessModifiers", "photoSize", "showPhotoMin")
    list_filter = ["selectedModule",]
    actions = [deleteSelectedPhotos]

admin.site.register(Albums, Albums_Admin)
admin.site.register(Photos, Photos_Admin)
