from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class StudentsConfig(AppConfig):

    name = 'students'
    verbose_name = _('Students database')

    def ready(self):
        from students import signals
