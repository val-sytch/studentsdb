from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from students.models import Student, Group


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):

        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', 'Надіслати'))

    from_email = forms.EmailField(label=_('Your e-mail'))
    subject = forms.CharField(label=_('Theme'), max_length=128)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # set form tag attributes
        if kwargs['instance'] is not None:
            add_form = False
        else:
            add_form = True

        if add_form:
            self.helper.form_action = reverse('student_add')
        else:
            self.helper.form_action = reverse('student_edit', kwargs={'pk': kwargs['instance'].id})

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.add_input(Submit('add_button', _('Save'), css_class='btn btn-primary'))
        self.helper.add_input(Submit('cancel_button', _('Cancel'), css_class='btn btn-link'))

    def clean_student_group(self):
        """
        Check if student is leader in any group.
        If yes, then ensure it’s the same as selected group.
        """
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise forms.ValidationError(_('This student is already leader of another group'), code='invalid')
        return self.cleaned_data['student_group']


class GroupUpdateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # set form tag attributes
        if kwargs['instance'] is not None:
            add_form = False
        else:
            add_form = True

        if add_form:
            self.helper.form_action = reverse('group_add')
        else:
            self.helper.form_action = reverse('group_edit', kwargs={'pk': kwargs['instance'].id})

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.add_input(Submit('add_button', _('Save'), css_class='btn btn-primary'))
        self.helper.add_input(Submit('cancel_button', _('Cancel'), css_class='btn btn-link'))

    def clean_leader(self):
        """
        Check if student, who is selected to be leader in group, belongs to this group.
        To be selected as a leader, student have to be previously assigned to the group
        """
        #
        students = Student.objects.filter(student_group=self.instance)
        if students and self.cleaned_data['leader'] and not students.filter(id=self.cleaned_data['leader'].id).exists():
            raise forms.ValidationError(_('This student belongs to another group'), code='invalid')
        return self.cleaned_data['leader']

