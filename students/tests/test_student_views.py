from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from students.models import Student, Group


class TestStudentList(TestCase):

    fixtures = ['test_data.json']

    def setUp(self):

        # remember test browser
        self.client = Client()

        # remember url to our homepage
        self.url = reverse('students_list')

    def test_students_list(self):
        # make request to the server to get homepage page
        response = self.client.get(self.url)

        # have we received OK status from the server?
        self.assertEqual(response.status_code, 200)

        # do we have student name on a page?
        self.assertContains(response, 'Vitaliy')

        # do we have link to student edit form?
        self.assertContains(response, reverse('student_edit', kwargs={'pk': Student.objects.all()[0].id}))

        # ensure we got 3 students, pagination limit is 3
        self.assertEqual(len(response.context['students']), 3)

    def test_current_group(self):
        # set group1 as currently selected group
        group = Group.objects.filter(title="MTM1")[0]
        self.client.cookies['current_group'] = group.id

        # make request to the server to get homepage page
        response = self.client.get(self.url)

        # in group1 we have only 1 student
        self.assertEqual(len(response.context['students']), 1)

    def test_order_by(self):
        # set order by Last Name
        response = self.client.get(self.url, {'order_by': 'last_name'})

        # now check if we got proper order
        students = response.context['students']
        self.assertEqual(students[0].last_name, 'Markiv')
        self.assertEqual(students[1].last_name, 'Melnicov')
        self.assertEqual(students[2].last_name, 'Nelson')

    def test_reverse_order_by(self):
        # order students by ticket number in reverse order
        response = self.client.get(self.url, {'order_by': 'ticket',
            'reverse': '1'})

        # now check if we got proper order
        students = response.context['students']
        self.assertEqual(students[0].last_name, 'Markiv')
        self.assertEqual(students[1].last_name, 'Melnicov')
        self.assertEqual(students[2].last_name, 'Podoba')

    def test_pagination(self):
        # navigate to second page with students
        response = self.client.get(self.url, {'page': '2'})

        self.assertEqual(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['students']), 1)
        self.assertEqual(response.context['students'][0].last_name, 'Nelson')
