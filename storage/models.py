# -*- coding: utf-8 -*-

from django.db import models
from plushcms.settings import MEDIA_STORAGE

from os import remove
from os import rename
from os import mkdir
from os import chmod
from os.path import exists

from shutil import rmtree
from shutil import move

from plushcms.storage.storagelib import getDirectoryUploadPath

# Required for using raw SQL calls
from django.db import connection
from django.db import transaction

class Directories(models.Model):
    """Directory model"""
    title = models.CharField(max_length = 150, verbose_name = "Directory", unique = True, help_text = "Enter a name which doesn't exceed 150 characters.")
    directory = models.CharField(max_length = 150, unique = True, editable = False)
    accessModifiers = ((0, "Public directory"), (1, "Private directory"), (2, "Protected directory"))
    selectedModule = models.IntegerField(max_length = 150, verbose_name = "Access modifiers", choices = accessModifiers, blank = False, null = False, default = 0, help_text = u"Choose the module. Default value is public.")

    class Meta:
        verbose_name = "directory"
        verbose_name_plural = "directories"

    def mod(self):
        if self.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\" \> %s" % self.accessModifiers[0][1]
        elif self.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\" \> %s" % self.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\" \> %s" % self.accessModifiers[2][1]

    mod.allow_tags = True

    def save(self, force_insert = False, force_update = False):
        # Creating upload directory
        if not exists(MEDIA_STORAGE):
            mkdir(MEDIA_STORAGE)

        self.directory = self.title.lower().replace(" ", "-")

        # Creating new directory or changing access modifiers flag
        if not exists("%s/%s" % (MEDIA_STORAGE, self.directory)):
            if self.selectedModule == 0 or self.selectedModule == 1:
                mkdir("%s/%s" % (MEDIA_STORAGE, self.directory), 0755)
            else:
                mkdir("%s/%s" % (MEDIA_STORAGE, self.directory), 0200)
        else:
            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod("%s/%s" % (MEDIA_STORAGE, self.directory), 0755)
            else:
                chmod("%s/%s" % (MEDIA_STORAGE, self.directory), 0200)
        
        # Renaming directory or updating all files path
        if self.id:
            prevDirectory = Directories.objects.raw("SELECT * FROM storage_directories WHERE id = %s" % self.id)
            prevFiles = Directories.objects.raw("SELECT * FROM storage_files WHERE parent_id = %s" % self.id)
            numberOfFiles = Files.objects.filter(parent = self).count()

            cursor = connection.cursor()

            for x in xrange(numberOfFiles):
                cursor.execute("UPDATE storage_files SET file = \"%s\" WHERE id = %s" % (prevFiles[x].file.replace(prevDirectory[0].directory, self.directory), prevFiles[x].id))

            transaction.commit_unless_managed()

            # Renaming directory
            rename("%s/%s" % (MEDIA_STORAGE, prevDirectory[0].directory), "%s/%s" % (MEDIA_STORAGE, self.directory))

            # Changing access modifiers flag for directory
            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod("%s/%s" % (MEDIA_STORAGE, self.directory), 0755)
            else:
                chmod("%s/%s" % (MEDIA_STORAGE, self.directory), 0200)

        super(Directories, self).save(force_insert, force_update)

    def delete(self):
        chmod("%s/%s" % (MEDIA_STORAGE, self.directory), 0755)
        rmtree("%s/%s" % (MEDIA_STORAGE, self.directory))

        super(Directories, self).delete()

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return unicode(self.title)

class Files(models.Model):
    """Files model"""
    parent = models.ForeignKey(Directories, verbose_name = "Directory", blank = False, null = False, default = 0, help_text = "Choose the directory.")
    title = models.CharField(max_length = 100, verbose_name = "Name", help_text = "Enter a name which doesn't exceed 100 characters.")
    description = models.TextField(verbose_name = "Description")
    file = models.FileField(upload_to = getDirectoryUploadPath, verbose_name = "File", help_text = "All file extensions and filetypes are allowed.")
    accessModifiers = ((0, "Public file"), (1, "Private file"), (2, "Protected file"))
    selectedModule = models.IntegerField(max_length = 150, verbose_name = "Access modifiers", choices = accessModifiers, blank = False, null = False, default = 0, help_text = "Choose the module. Default value is public.")
    fileSize = models.DecimalField(verbose_name = "File size (MB)", blank = False, editable = False, default = 0, max_digits = 5, decimal_places = 3)

    class Meta:
        verbose_name = "file"
        verbose_name_plural = "files"

    def showDirectoryAccessModifiers(self):
        if self.parent.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\" \> %s" % self.parent.accessModifiers[0][1]
        elif self.parent.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\" \> %s" % self.parent.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\" \> %s" % self.parent.accessModifiers[2][1]

    showDirectoryAccessModifiers.short_description = "Directory access modifier"
    showDirectoryAccessModifiers.allow_tags = True

    def showFileName(self):
        return unicode(self.file.path.split("/")[-1:][0])

    showFileName.short_description = "File name"

    def showFileAccessModifiers(self):
        if self.selectedModule == 0:
            return "<img src=\"/img/icons/public.png\" \> %s" % self.accessModifiers[0][1]
        elif self.selectedModule == 1:
            return "<img src=\"/img/icons/private.png\" \> %s" % self.accessModifiers[1][1]
        else:
            return "<img src=\"/img/icons/protected.png\" \> %s" % self.accessModifiers[2][1]

    showFileAccessModifiers.short_description = "File access modifier"
    showFileAccessModifiers.allow_tags = True

    def showFileAddress(self):
        if self.selectedModule == 2 or self.parent.selectedModule == 2:
            return "<div style=\"text-align: center;\">Unavailable</div>"
        else:
            index = self.file.path.find("img")
            return u"<div style=\"text-align: center;\"><a href=\"/%s\">Get it</a></div>" % self.file.path[index:]

    showFileAddress.short_description = "File address"
    showFileAddress.allow_tags = True
 
    def save(self, force_insert = False, force_update = False):
        # For the first time file upload
        if not self.id:
            if self.parent.selectedModule == 2:
                chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0755)

            self.fileSize = str(self.file.size / (1024 * 1024.0))

            super(Files, self).save(force_insert, force_update)

            if self.selectedModule == 0 or self.selectedModule == 1:
                chmod(self.file.path, 0755)
            else:
                chmod(self.file.path, 0200)

            if self.parent.selectedModule == 2:
                chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0200)

        else:
            prevSignleFile = "SELECT * from storage_files WHERE id = %s" % self.id
            prevSignleFile = Files.objects.raw(prevSignleFile)

            # If directories are identical
            if prevSignleFile[0].parent == self.parent:
                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, prevSignleFile[0].parent.directory), 0755)

                # If files are different
                if prevSignleFile[0].file != self.file:
                    chmod("%s" % prevSignleFile[0].file.path, 0755)
                    remove("%s" % prevSignleFile[0].file.path)

                    super(Files, self).save(force_insert, force_update)

                    self.fileSize = str(self.file.size / (1024 * 1024.0))

                # If files are identical
                elif prevSignleFile[0].file == self.file:
                    super(Files, self).save(force_insert, force_update)

                if self.selectedModule == 0 or self.selectedModule == 1:
                    chmod(self.file.path, 0755)
                else:
                    chmod(self.file.path, 0200)

                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, prevSignleFile[0].parent.directory), 0200)

            # If directories are different
            elif prevSignleFile[0].parent != self.parent:
                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0755)
                if prevSignleFile[0].parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, prevSignleFile[0].parent.directory), 0755)

                # If files are identical
                if prevSignleFile[0].file == self.file:                 
                    chmod("%s" % prevSignleFile[0].file.path, 0755)

                    self.file = unicode(self.file).replace(prevSignleFile[0].parent.directory, self.parent.directory)

                    move(prevSignleFile[0].file.path, self.file.path)

                # If files are different
                elif prevSignleFile[0].file != self.file:
                    oldPaths = (prevSignleFile[0].file.path, prevSignleFile[0].parent)

                    super(Files, self).save(force_insert, force_update)

                    chmod(oldPaths[0], 0755)
                    remove(oldPaths[0])                    

                    self.fileSize = str(self.file.size / (1024 * 1024.0))

                    if oldPaths[1].selectedModule == 2:
                        chmod("%s/%s" % (MEDIA_STORAGE, oldPaths[1].directory), 0200)

                if self.selectedModule == 0 or self.selectedModule == 1:
                    chmod(self.file.path, 0755)
                else:
                    chmod(self.file.path, 0200)

                if self.parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0200)
                if prevSignleFile[0].parent.selectedModule == 2:
                    chmod("%s/%s" % (MEDIA_STORAGE, prevSignleFile[0].parent.directory), 0200)                    

        super(Files, self).save(force_insert, force_update)

    def delete(self):
        if self.parent.selectedModule == 2:
            chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0755)
            remove(self.file.path)
            chmod("%s/%s" % (MEDIA_STORAGE, self.parent.directory), 0200)
        else:
            remove(self.file.path)

        super(Files, self).delete()

    def __str__(self):
        return str(self.showFileName())

    def __unicode__(self):
        return unicode(self.showFileName())
