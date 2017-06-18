from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from students.forms import GroupUpdateForm
from students.models import Group
from students.util import get_current_group


class GroupsListView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'students/groups_list.html'
    paginate_by = 3

    def get_queryset(self):
        # check if we need to show only one group of students
        current_group = get_current_group(self.request)
        if current_group:
            groups = Group.objects.filter(id=current_group.id)
        else:
            # otherwise show all students
            groups = super(GroupsListView, self).get_queryset()

        # try to order groups list
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('title', 'leader'):
            groups = groups.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                students = groups.reverse()
        return groups


class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Group was successfully saved')
        )
        return reverse('groups_list')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('groups_list'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Group was successfully saved')
        )
        return reverse('groups_list')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(
                self.request,
                messages.INFO,
                _('Editing of group was canceled')
            )
            return HttpResponseRedirect(reverse('groups_list'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Group was successfully deleted')
        )
        return reverse('groups_list')