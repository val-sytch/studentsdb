from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models import Student


def students_list(request):

    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    context = {
        'students': students
    }

    return render(request, 'students/students_list.html', context)


def student_add(request):
    pass


def student_edit(request):
    pass


def student_delete(request):
    pass