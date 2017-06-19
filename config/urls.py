from django.conf.urls import url, include
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve

from config.settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    # students database
    url(r'', include('students.urls')),

    # User Related urls(login, logout, registration)
    url(r'', include('stud_auth.urls')),

    # internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['students']), name='javascript_catalog'),

    url(r'^admin/', admin.site.urls),
]

if DEBUG:
    # serve files from media folder
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})]
