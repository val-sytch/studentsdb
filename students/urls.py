from django.conf.urls import url

from .views import groups, students, journal

urlpatterns = [

    # URL pattern for students
    url(
        regex=r'^$',
        view=students.students_list,
        name='students_list'
    ),
    url(
        regex=r'^student/add/$',
        view=students.student_add,
        name='student_add'
    ),
    url(
        regex=r'^student/(?P<sid>\d+)/edit/$',
        view=students.student_edit,
        name='student_edit'
    ),
    url(
        regex=r'^student/(?P<sid>\d+)/delete/$',
        view=students.student_delete,
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
        regex=r'^group/(?P<gid>\d+)/edit/$',
        view=groups.group_edit,
        name='group_edit'
    ),
    url(
        regex=r'^group/(?P<gid>\d+)/delete/$',
        view=groups.group_delete,
        name='group_delete'
    ),
]
