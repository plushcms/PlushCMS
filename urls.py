# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings

handler500 = "plushcms.core.views.error500"
handler404 = "plushcms.core.views.error404"

urlpatterns = patterns("",
    url(r"", include("plushcms.core.urls")),
    url(r"img/(?P<path>.*)$", "django.views.static.serve", {"document_root" : settings.MEDIA_ROOT}),
)
