from django.apps import AppConfig


class StudentsConfig(AppConfig):

    name = 'students'
    verbose_name = 'База Студентів'

    def ready(self):
        from students import signals
