from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student, Group


class Command(BaseCommand):

    help = 'Prints to console number of student related objects in a database(student,group,user)'
    models = (('student', Student), ('group', Group), ('user', User))

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        for name, model in self.models:
            if name in options['model']:
                self.stdout.write('Number of {}s in database: {:d}'.format(name, model.objects.count()))
