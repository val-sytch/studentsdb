from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

from students.models import Student, Group


@override_settings(LANGUAGE_CODE='en')
class TestStudentUpdateForm(TestCase):

    fixtures = ['test_data.json']

    def setUp(self):
        # remember test browser
        self.client = Client()

        # remember url to edit form
        self.url = reverse('student_edit', kwargs={'pk': 1})

    def test_form(self):
        # login as admin to access student edit form
        self.client.login(username='admin', password='root12345')

        # get form and check few fields there
        response = self.client.get(self.url)

        # check response status
        self.assertEqual(response.status_code, 200)

        # check page title, few field titles and button on edit form
        self.assertContains(response, 'Edit student')
        self.assertContains(response, 'Ticket')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'name="add_button"')
        self.assertContains(response, 'name="cancel_button"')
        self.assertContains(response, 'action="{}"'.format(self.url))

    def test_success(self):
        # login as admin to access student edit form
        self.client.login(username='admin', password='root12345')

        # post form with valid data
        group = Group.objects.filter(title='MTM1')[0]
        response = self.client.post(self.url, {'first_name': 'Updated Name',
            'last_name': 'Updated Last Name', 'ticket': '567',
            'student_group': group.id, 'birthday': '1990-11-11'}, follow=True)

        # check response status
        self.assertEqual(response.status_code, 200)

        # test updated student details
        student = Student.objects.get(pk=1)
        self.assertEqual(student.first_name, 'Updated Name')
        self.assertEqual(student.last_name, 'Updated Last Name')
        self.assertEqual(student.ticket, '567')
        self.assertEqual(student.student_group, group)

        # check proper redirect after form post
        self.assertContains(response, 'Student was successfully saved')
    
    def test_cancel(self):
        # login as admin to access student edit form
        self.client.login(username='admin', password='root12345')

        # post form with Cancel button
        response = self.client.post(self.url, {'cancel_button': 'Cancel'},
            follow=True)

        self.assertContains(response, 'Editing of student was canceled')

    def test_access(self):
        # try to access form as anonymous user
        response = self.client.get(self.url, follow=True)

        # we have to get 200 code and login form
        self.assertEqual(response.status_code, 200)

        # check that we're on login form
        self.assertContains(response, 'Login Form')

        # check redirect url
        self.assertEqual(response.redirect_chain[0],
            ('/users/login/?next=/student/1/edit/', 302))
    #
    def test_styles(self):
        # login as admin to access student edit form
        self.client.login(username='admin', password='root12345')

        # get form and check few fields there
        response = self.client.get(self.url)

        # check response status
        self.assertEqual(response.status_code, 200)

        # check classes
        self.assertContains(response, 'form-horizontal')
        self.assertContains(response, 'form-group')
        self.assertContains(response, 'control-label')
        self.assertContains(response, 'controls')
        self.assertContains(response, 'btn-primary')
