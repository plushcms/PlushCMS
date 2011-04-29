About PlushCMS
==============

PlushCMS is a [Python](http://python.org/) based Content Management System with Django's admin interface.  
At this stage it's dedicated as a blogging platform or portal management system.

PlushCMS basic feature list
---------------------------

Currently, the main modules available for PlushCMS cover the following fields of activity:

### a) auth application (build-in Django)
* [http://docs.djangoproject.com/en/dev/topics/auth/](http://docs.djangoproject.com/en/dev/topics/auth/)

### b) core application
* Categories
* Comments (captcha protection systems)
* Links
* News (multiple category, working copy flag, top news flag)
* Partners (auto logo resize)
* Subpages (Standard subpage, Contact form with captcha protection systems, *Gallery module, *Storage module)
* RSS 2.0
* Search engine (comparison with title and content of news and subpage)
* Pagination (news, search results, news from category)

*gallery and storage application required

### c) gallery application
* Albums (auto scale photos, access modifiers)
* Photos (validate photo file upload, access modifiers)

### d) storage application
* Directories (access modifiers)
* Files (validate file upload, access modifiers)

### e) modified treemenus application
* dynamic menu and sub-menu (changing ranks)

Extras
------
* [TinyMCE](http://tinymce.moxiepre.com/) (WYSIWYG Editor)
* [pygments](http://pygments.org/) (Generic Syntax Highlighter)
* [Treemenus](http://pre.google.com/p/django-treemenus/) (Generic tree-structured menuing system)

How to install (on localhost)?
==============================

1. Download PlushCMS v0.1.1 from Github
2. Configure DATABASES dict in settings.py
3. Configure contact form in settings.py (if you want to use Contact form module)
4. Set MEDIA\_ROOT, MEDIA\_GALLERY, MEDIA\_STORAGE, MEDIA\_FONT, MEDIA\_URL, TEMPLATE\_DIRS in settings.py just like the example:
    <pre># JavaScript, CSS nad image reference path ("/img" is static)
    MEDIA_ROOT = "/home/username/plushcms/img"</pre>

     <pre># Upload photos directory ("/img/photoGallery" is static)
    MEDIA_GALLERY = "/home/username/plushcms/img/photoGallery"</pre>

     <pre># Upload files directory ("/img/uploadFiles" is static)
    MEDIA_STORAGE = "/home/username/plushcms/img/uploadFiles"</pre>

     <pre># Font file path used by captcha image generator ("/img/fonts/captcha.ttf" is static)
    MEDIA_FONT = "/home/username/plushcms/img/fonts/captcha.ttf"</pre>

     <pre># URL used for managing stored files ("/img/" is static)
    MEDIA_URL = "/home/username/plushcms/img/"</pre>

     <pre># Templates path ("/core/templates/" is static)
    TEMPLATE_DIRS = (
        "/home/username/plushcms/core/templates/",
    )</pre>
5. Create new database:
    <pre>python manage.py syncdb</pre>
6. Run the developer server:
    <pre>python manage.py runserver</pre>
7. Add "Main menu" in Treemenus application
8. Enjoy (:!

Details
=======

Version: **0.1.1**  
Release date: **29.04.2011**  
Requirements: **Python 2.5+**, **Django 1.2+**, **PIL 1.1.7**

Team
====

[Piotr Tynecki](https://github.com/katharsis) (piotr@tynecki.pl)  
[Paweł Topór](https://github.com/toporek) (pawel@ptopor.pl)

Licence
=======

The full text of the license can be found in the **LICENCE** file.
