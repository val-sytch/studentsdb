from django.conf.urls import url

from .views import groups, students, journal, contact_admin

urlpatterns = [

    # URL pattern for students
    url(
        regex=r'^$',
        view=students.StudentsListView.as_view(),
        name='students_list'
    ),
    url(
        regex=r'^student/add/$',
        view=students.StudentCreateView.as_view(),
        name='student_add'
    ),
    url(
        regex=r'^student/(?P<pk>\d+)/edit/$',
        view=students.StudentUpdateView.as_view(),
        name='student_edit'
    ),
    url(
        regex=r'^student/(?P<pk>\d+)/delete/$',
        view=students.StudentDeleteView.as_view(),
        name='student_delete'
    ),

    # URL pattern for groups
    url(
        regex=r'^groups/$',
        view=groups.groups_list,
        name='groups_list'
    ),
    url(
        regex=r'^group/add/$',
        view=groups.group_add,
        name='group_add'
    ),
    url(
        regex=r'^group/(?P<pk>\d+)/edit/$',
        view=groups.group_edit,
        name='group_edit'
    ),
    url(
        regex=r'^group/(?P<pk>\d+)/delete/$',
        view=groups.group_delete,
        name='group_delete'
    ),

    # Contact Admin Form
    url(
        regex=r'^contact-admin/$',
        view=contact_admin.ContactView.as_view(),
        name='contact_admin'),
]
