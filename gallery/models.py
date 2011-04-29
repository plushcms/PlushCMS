# -*- coding: utf-8 -*-

from django.db import models
from plushcms.settings import MEDIA_GALLERY

from os import makedirs
from os import remove
from os import rename
from os import mkdir
from os import chmod
from os.path import exists
from shutil import rmtree
from shutil import move

from plushcms.plushlib import scaleImage
from plushcms.plushlib import getFileSize

from plushcms.gallery.gallerylib import getAlbumUploadPath

# Required for using raw SQL calls
from django.db import connection
from django.db import transaction

from django.core.exceptions import ValidationError

# Used by Albums model
def widthPhotoValidator(value):
    if value < 640:
        raise ValidationError("The minimum value for this field is 640.")
    elif value > 1600:
        raise ValidationError("The maximum value for this field is 1600.")

# Used by Albums model
def heightPhotoValidator(value):
    if value < 480:
        raise ValidationError("The minimum value for this field is 480.")
    elif value > 1200:
        raise ValidationError("The maximum value for this field is 1200.")

class Albums(models.Model):
    """Photo album model"""
    title = models.CharField(max_length = 150, verbose_name = "Album", unique = True, help_text = "Enter a title which doesn't exceed 150 characters.")
    directory = models.CharField(max_length = 150, unique = True, editable = False)
    widthPhoto = models.PositiveIntegerField(max_length = 150, verbose_name = "Width", help_text = "Enter the photo width. Default value is 800px", default = 800, validators = [widthPhotoValidator])
    heightPhoto = models.PositiveIntegerField(max_length = 150, verbose_name = "Height", help_text = "Enter the photo height. Default value is 600px", default = 600, validators = [heightPhotoValidator])
    accessModifiers = ((0, "Public album"), (1, "Private album"), (2, "Protected album"))
    selectedModule = models.IntegerField(max_length = 150, verbose_name = "Access modifiers", choices = accessModifiers, blank = False, null = False, default = 0, help_text = "Choose the module. Default value is public.")

    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albums"

    def mod(self):
        if self.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\"> %s" % self.accessModifiers[0][1]
        elif self.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\"> %s" % self.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\"> %s" % self.accessModifiers[2][1]

    mod.allow_tags = True
    mod.short_description = "Access modifiers"

    def save(self, force_insert = False, force_update = False):
        # Creating photoGallery directory
        if not exists(MEDIA_GALLERY):
            mkdir(MEDIA_GALLERY)

        self.directory = self.title.lower().replace(" ", "-")
        fullPathDirectory = "%s/%s" % (MEDIA_GALLERY, self.directory)

        # Creating new photo album or changing access modifiers flag
        if not exists(fullPathDirectory):
            if self.selectedModule == 0 or self.selectedModule == 1:
                mkdir(fullPathDirectory, 0755)
            else:
                mkdir(fullPathDirectory, 0200)
        else:
            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod(fullPathDirectory, 0755)
            else:
                chmod(fullPathDirectory, 0200)

        # Renaming photo album or updating all photos path
        if self.id:
            prevAlbum = Albums.objects.raw("SELECT * FROM gallery_albums WHERE id = %s" % self.id)
            prevPhotos = Albums.objects.raw("SELECT * FROM gallery_photos WHERE parent_id = %s" % self.id)
            numberOfPhotos = Photos.objects.filter(parent = self).count()

            cursor = connection.cursor()

            for x in xrange(numberOfPhotos):
                cursor.execute("UPDATE gallery_photos SET photo = \"%s\", photoMin = \"%s\" WHERE id = %s" % (prevPhotos[x].photo.replace(prevAlbum[0].directory, self.directory), prevPhotos[x].photoMin.replace(prevAlbum[0].directory, self.directory), prevPhotos[x].id))

            transaction.commit_unless_managed()

            # Renaming photo album
            rename("%s/%s" % (MEDIA_GALLERY, prevAlbum[0].directory), fullPathDirectory)

            # Changing access modifiers flag for photo album
            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod(fullPathDirectory, 0755)
            else:
                chmod(fullPathDirectory, 0200)

        super(Albums, self).save(force_insert, force_update)

    def delete(self):
        chmod("%s/%s" % (MEDIA_GALLERY, self.directory), 0755)
        rmtree("%s/%s" % (MEDIA_GALLERY, self.directory))

        super(Albums, self).delete()

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

class Photos(models.Model):
    """Photos model"""
    parent = models.ForeignKey(Albums, verbose_name = "Album", blank = False, null = False, default = 0, help_text = "Choose the album.")
    description = models.TextField(verbose_name = "Description")
    photo = models.ImageField(upload_to = getAlbumUploadPath, verbose_name = "Photo", help_text = "Only image uploads are allowed.")
    photoMin = models.ImageField(upload_to = getAlbumUploadPath, editable = False)
    accessModifiers = ((0, "Public photo"), (1, "Private photo"), (2, "Protected photo"))
    selectedModule = models.IntegerField(max_length = 150, verbose_name = "Access modifiers", choices = accessModifiers, blank = False, null = False, default = 0, help_text = "Choose the module. Default value is public.")
    photoSize = models.DecimalField(verbose_name = "Photo size (MB)", blank = False, editable = False, default = 0, max_digits = 5, decimal_places = 3)

    thumbnailSize = 122

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"

    def showPhotoName(self):
        return "%s" % self.photo.path.split("/")[-1:][0]

    showPhotoName.short_description = "File name"

    def showAlbumAccessModifiers(self):
        if self.parent.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\" /> %s" % self.parent.accessModifiers[0][1]
        elif self.parent.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\" /> %s" % self.parent.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\" /> %s" % self.parent.accessModifiers[2][1]

    showAlbumAccessModifiers.short_description = "Album access modifier"
    showAlbumAccessModifiers.allow_tags = True

    def showPhotoAccessModifiers(self):
        if self.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\" /> %s" % self.accessModifiers[0][1]
        elif self.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\" /> %s" % self.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\" /> %s" % self.accessModifiers[2][1]

    showPhotoAccessModifiers.short_description = "Photo access modifier"
    showPhotoAccessModifiers.allow_tags = True

    def showPhotoMin(self):
        if self.selectedModule == 2 or self.parent.selectedModule == 2:
            return "<div style=\"text-align: center;\">Unavailable</div>"
        else:
            tempPhotoPath = self.photo.path.split("/")
            link = u"<a href=\"/img/photoGallery/%s/%s\"><img src=\"/img/photoGallery/%s/%s\" /></a>" % (tempPhotoPath[-2], tempPhotoPath[-1], tempPhotoPath[-2], tempPhotoPath[-1].replace(".", "-min."))

            return link

    showPhotoMin.short_description = "Thumbnail"
    showPhotoMin.allow_tags = True

    def save(self, force_insert = False, force_update = False):
        # For the first time photo upload
        if not self.id:
            self.photoMin = u"photoGallery/%s/%s" % (self.parent.directory, str(self.photo).replace(".", "-min."))

            if self.parent.selectedModule == 2:
                chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0755)

            super(Photos, self).save(force_insert, force_update)
                
            scaleImage(self.photo.path, self.parent.widthPhoto)
            scaleImage(self.photo.path, self.thumbnailSize, 1)

            self.photoSize = getFileSize(self.photo.path)

            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod(self.photo.path, 0755)
                chmod(self.photoMin.path, 0755)
            else:
                chmod(self.photo.path, 0200)
                chmod(self.photoMin.path, 0200)

            if self.parent.selectedModule == 2:
                chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0200)

        else:
            prevSignlePhoto = "SELECT * from gallery_photos WHERE id = %s" % self.id
            prevSignlePhoto = Photos.objects.raw(prevSignlePhoto)

            # If albums are identical
            if prevSignlePhoto[0].parent == self.parent:
                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, prevSignlePhoto[0].parent.directory), 0755)

                # If photos are different
                if prevSignlePhoto[0].photo != self.photo:
                    chmod("%s" % prevSignlePhoto[0].photo.path, 0755)
                    chmod("%s" % prevSignlePhoto[0].photoMin.path, 0755)
                    remove("%s" % prevSignlePhoto[0].photo.path)
                    remove("%s" % prevSignlePhoto[0].photoMin.path)

                    super(Photos, self).save(force_insert, force_update)

                    scaleImage(self.photo.path, self.parent.widthPhoto)
                    scaleImage(self.photo.path, self.thumbnailSize, 1)

                    self.photoSize = getFileSize(self.photo.path)
                    self.photoMin = unicode(self.photo).replace(".", "-min.")

                # If photos are identical
                elif prevSignlePhoto[0].photo == self.photo:
                    super(Photos, self).save(force_insert, force_update)

                if self.selectedModule == 0 or self.selectedModule == 1:
                    chmod(self.photo.path, 0755)
                    chmod(self.photoMin.path, 0755)
                else:
                    chmod(self.photo.path, 0200)
                    chmod(self.photoMin.path, 0200)

                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, prevSignlePhoto[0].parent.directory), 0200)

            # If albums are different
            elif prevSignlePhoto[0].parent != self.parent:
                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0755)
                if prevSignlePhoto[0].parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, prevSignlePhoto[0].parent.directory), 0755)

                # If photos are identical
                if prevSignlePhoto[0].photo == self.photo:                 
                    chmod("%s" % prevSignlePhoto[0].photo.path, 0755)
                    chmod("%s" % prevSignlePhoto[0].photoMin.path, 0755)

                    self.photo = unicode(self.photo).replace(prevSignlePhoto[0].parent.directory, self.parent.directory)
                    self.photoMin = unicode(self.photoMin).replace(prevSignlePhoto[0].parent.directory, self.parent.directory)

                    move(prevSignlePhoto[0].photo.path, self.photo.path)
                    move(prevSignlePhoto[0].photoMin.path, self.photoMin.path)

                # If photos are different
                elif prevSignlePhoto[0].photo != self.photo:
                    oldPaths = (prevSignlePhoto[0].photo.path, prevSignlePhoto[0].photoMin.path, prevSignlePhoto[0].parent)

                    super(Photos, self).save(force_insert, force_update)

                    scaleImage(self.photo.path, self.parent.widthPhoto)
                    scaleImage(self.photo.path, self.thumbnailSize, 1)

                    chmod(oldPaths[0], 0755)
                    chmod(oldPaths[1], 0755)
                    remove(oldPaths[0])
                    remove(oldPaths[1])                    

                    self.photoSize = getFileSize(self.photo.path)
                    self.photoMin = unicode(self.photo).replace(".", "-min.")
                    
                    if oldPaths[2].selectedModule == 2:
                        chmod("%s/%s" % (MEDIA_GALLERY, oldPaths[2].directory), 0200)

                if self.selectedModule == 0 or self.selectedModule == 1:
                    chmod(self.photo.path, 0755)
                    chmod(self.photoMin.path, 0755)
                else:
                    chmod(self.photo.path, 0200)
                    chmod(self.photoMin.path, 0200)

                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0200)
                if prevSignlePhoto[0].parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_GALLERY, prevSignlePhoto[0].parent.directory), 0200)                    

        super(Photos, self).save(force_insert, force_update)

    def delete(self):
        if self.parent.selectedModule == 2:
            chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0755)
            remove(self.photo.path)
            remove(self.photoMin.path)
            chmod("%s/%s" % (MEDIA_GALLERY, self.parent.directory), 0200)
        else:
            remove(self.photo.path)
            remove(self.photoMin.path)

        super(Photos, self).delete()

    def __str__(self):
        return str(self.showPhotoName())

    def __unicode__(self):
        return unicode(self.showPhotoName())
