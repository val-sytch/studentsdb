from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from students.forms import StudentUpdateForm
from students.models import Student
from students.util import get_current_group


class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/students_list.html'
    paginate_by = 3

    def get_queryset(self):
        # check if we need to show only one group of students
        current_group = get_current_group(self.request)
        if current_group:
            students = Student.objects.filter(student_group=current_group)
        else:
            # otherwise show all students
            students = super(StudentsListView, self).get_queryset()

        # try to order students list
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = students.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                students = students.reverse()
        return students


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Student was successfully saved')
        )
        return reverse('students_list')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('students_list'))
        else:
            return super(StudentCreateView, self).post(request, *args, **kwargs)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Student was successfully saved')
        )
        return reverse('students_list')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(
                self.request,
                messages.INFO,
                _('Editing of student was canceled')
            )
            return HttpResponseRedirect(reverse('students_list'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.INFO,
            _('Student was successfully deleted')
        )
        return reverse('students_list')
