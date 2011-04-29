# -*- coding: utf-8 -*-

from django.contrib import admin

from plushcms.storage.models import Directories
from plushcms.storage.models import Files

from plushcms.storage.storagelib import deleteSelectedDirectories
from plushcms.storage.storagelib import deleteSelectedFiles

class Directories_Admin(admin.ModelAdmin):
    list_display = ("title", "mod")
    list_filter = ["selectedModule",]
    actions = [deleteSelectedDirectories]

class Files_Admin(admin.ModelAdmin):
    list_display = ("parent", "showDirectoryAccessModifiers", "showFileName", "showFileAccessModifiers", "fileSize", "showFileAddress")
    list_filter = ["selectedModule",]
    actions = [deleteSelectedFiles]

admin.site.register(Directories, Directories_Admin)
admin.site.register(Files, Files_Admin)
