import logging

from django.utils.six import StringIO
from django.test import TestCase

from students.models import Student


class StudentSignalsTests(TestCase):

    def test_log_student_crud(self):
        """Check logging signal for newly created student"""
        # add own root handler to catch student signals output
        out = StringIO()
        handler = logging.StreamHandler(out)
        logging.root.addHandler(handler)

        # now create student, this should raise new message inside
        # our logger output file
        student = Student(first_name='Demo', last_name='Student')
        student.save()

        # check output file content
        out.seek(0)
        self.assertTrue('Student added:' in out.readlines()[-1])

        # now update existing student and check last line in out
        student.ticket = '12345'
        student.save()
        out.seek(0)
        self.assertTrue('Student updated:' in out.readlines()[-1])

        # delete existing student and check logger output
        student.delete()
        out.seek(0)
        self.assertTrue('Student deleted:' in out.readlines()[-1])
        # remove our handler from root logger
        logging.root.removeHandler(handler)
