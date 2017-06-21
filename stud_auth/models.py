from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class StudentProfile(models.Model):
    """
    To keep extra user data
    """
    # user mapping
    user = models.OneToOneField(User)

    class Meta(object):
        verbose_name = _('User Profile')

    # extra user data
    mobile_phone = models.CharField(max_length=12, blank=True, verbose_name=_('Mobile Phone'), default='')

    def __str__(self):
        return self.user.username