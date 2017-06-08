from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.core.urlresolvers import reverse

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

    from_email = forms.EmailField(label='Ваша Емейл Адреса')
    subject = forms.CharField(label='Заголовок листа', max_length=128)
    message = forms.CharField(label='Текст повідомлення', widget=forms.Textarea)


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
        self.helper.add_input(Submit('add_button', 'Зберегти', css_class='btn btn-primary'))
        self.helper.add_input(Submit('cancel_button', 'Скасувати', css_class='btn btn-link'))