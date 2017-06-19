from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


# User Related urls
urlpatterns = [
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'students_list'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='students_list'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
]
