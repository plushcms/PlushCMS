# -*- coding: utf-8 -*-

from plushcms.settings import MEDIA_STORAGE

from os import chmod

# Delete selected directories in Admin Panel
def deleteSelectedDirectories(modeladmin, request, queryset):
    [chmod("%s/%s" % (MEDIA_STORAGE, x.directory), 0755) for x in queryset]
    [x.delete() for x in queryset]

    numberOfDeleted = len(queryset)

    if numberOfDeleted == 1:
        info = "Deleted 1 directory."
    else:
        info = "Deleted %d directories." % numberOfDeleted

    modeladmin.message_user(request, info)

deleteSelectedDirectories.short_description = "Delete selected directories"

# Delete selected files in Admin Panel
def deleteSelectedFiles(modeladmin, request, queryset):
    [x.delete() for x in queryset]

    numberOfDeleted = len(queryset)

    if numberOfDeleted == 1:
        info = "Deleted 1 file."
    else:
        info = "Deleted %d files." % numberOfDeleted

    modeladmin.message_user(request, info)

deleteSelectedFiles.short_description = "Delete selected files"

# Define the upload_to option
def getDirectoryUploadPath(instance, filename):
    return "%s/%s/%s" % (MEDIA_STORAGE, instance.parent.directory, filename)
