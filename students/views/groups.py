from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models import Group


def groups_list(request):
    groups = Group.objects.all()

    # try to order group list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate students
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)

    context = {
        'groups': groups
    }
    return render(request, 'students/groups_list.html', context)


def group_add(request):
    pass


def group_edit(request):
    pass


def group_delete(request):
    pass