from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from students.models import Student, Group, MonthJournal


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """
        Check if student is leader in any group.
        If yes, then ensure it’s the same as selected group.
        """
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError('Студент є старостою іншої групи.', code='invalid')
        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):

    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    # possibility to duplicate all selected students to db
    actions = ['copy_student']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('student_edit', kwargs={'pk': obj.id})

    def copy_student(self, request, queryset):
        rows_updated = 0
        for obj in queryset:
            obj.pk = None
            obj.first_name += '(copy)'
            obj.save()
            rows_updated += 1
        if rows_updated == 1:
            message_bit = "1 студент був успiшно скопiйований"
        else:
            message_bit = "{} студенти були успiшно скопiйованi".format(rows_updated)
        self.message_user(request, message_bit)
    copy_student.short_description = "Скопiювати обраних студентiв"


class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        """
        Check if student, who is selected to be leader in group, belongs to this group.
        To be selected as a leader, student have to be previously assigned to the group
        """
        #
        students = Student.objects.filter(student_group=self.instance)
        if students and not students.filter(id=self.cleaned_data['leader'].id).exists():
            raise ValidationError('Цей cтудент належить до іншої групи.', code='invalid')
        return self.cleaned_data['leader']


class GroupAdmin(admin.ModelAdmin):

    list_display = ['title', 'leader']
    list_display_links = ['title']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title']
    form = GroupFormAdmin

    def view_on_site(self, obj):
        return reverse('group_edit', kwargs={'pk': obj.id})


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(MonthJournal)

