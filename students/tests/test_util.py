from datetime import datetime

from django.http import HttpRequest
from django.test import TestCase

from students.models import Student, Group
from students.util import get_current_group, get_groups, paginate


class UtilsTestCase(TestCase):
    """Test functions from util module"""

    def setUp(self):
        # create group
        group1, created = Group.objects.get_or_create(id=1, title='Group1')
        group2, created = Group.objects.get_or_create(id=2, title="Group2")

        # create student
        student, created = Student.objects.get_or_create(
            id=1,
            first_name="Vitaliy",
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='12345')

    def test_get_current_group(self):
        request = HttpRequest()
        # test with no group set in cookie
        request.COOKIES['current_group'] = ''
        self.assertEqual(None, get_current_group(request))
        # test with invalid group id
        request.COOKIES['current_group'] = '12345'
        self.assertEqual(None, get_current_group(request))
        # test with proper group identificator
        group = Group.objects.filter(title='Group1')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertEqual(group, get_current_group(request))

    def test_get_groups(self):
        request = HttpRequest()

        self.assertEqual(len(get_groups(request)), 2)
        self.assertFalse(get_groups(request)[0]['selected'])

        group = Group.objects.filter(title='Group1')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertTrue(get_groups(request)[0]['selected'])

    def test_paginate(self):
        # this dictionary will serve as template context
        context = {}

        # prepare test request
        request = HttpRequest()

        # check PageNotAnInteger case: ab string
        request.GET['page'] = 'ab'
        result = paginate([1, 2, 3, 4], 3, request, context,
                          var_name='object_list')
        self.assertEqual(len(result['object_list']), 3)
        self.assertEqual(result['is_paginated'], True)
        self.assertEqual(len(result['page_obj']), 3)
        self.assertEqual(result['object_list'][0], 1)
        self.assertEqual(result['object_list'][1], 2)
        self.assertEqual(result['object_list'][2], 3)

        # check empty page case: should be last page
        request.GET['page'] = '9999'
        result = paginate([1, 2, 3, 4], 3, request, context,
                          var_name='object_list')
        self.assertEqual(len(result['object_list']), 1)
        self.assertEqual(result['object_list'][0], 4)

        # check valid page: second page
        request.GET['page'] = '2'
        result = paginate([1, 2, 3, 4, 5], 3, request, context,
                          var_name='my_list')
        self.assertEqual(len(result['my_list']), 2)
        self.assertEqual(result['my_list'][0], 4)
        self.assertEqual(result['my_list'][1], 5)
