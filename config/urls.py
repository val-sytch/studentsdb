from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from config.settings import MEDIA_ROOT, DEBUG

urlpatterns = [

    url(r'^', include('students.urls')),

    url(r'^admin/', admin.site.urls),
]


if DEBUG:
    # serve files from media folder
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})]
