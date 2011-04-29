# -*- coding: utf-8 -*-

from plushcms.settings import MEDIA_GALLERY

from os import chmod

# Delete selected albums in Admin Panel
def deleteSelectedAlbums(modeladmin, request, queryset):
    [chmod("%s/%s" % (MEDIA_GALLERY, x.directory), 0755) for x in queryset]
    [x.delete() for x in queryset]

    numberOfDeleted = len(queryset)

    if numberOfDeleted == 1:
        info = "Deleted 1 album."
    else:
        info = "Deleted %d albums." % numberOfDeleted

    modeladmin.message_user(request, info)

deleteSelectedAlbums.short_description = "Delete selected albums"

# Delete selected photos in Admin Panel
def deleteSelectedPhotos(modeladmin, request, queryset):
    [x.delete() for x in queryset]

    numberOfDeleted = len(queryset)

    if numberOfDeleted == 1:
        info = "Deleted 1 photo."
    else:
        info = "Deleted %d photos." % numberOfDeleted

    modeladmin.message_user(request, info)

deleteSelectedPhotos.short_description = "Delete selected photos"

# Define the upload_to option
def getAlbumUploadPath(instance, filename):
    return "%s/%s/%s" % ("photoGallery", instance.parent.directory, filename)
