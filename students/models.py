# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):

    first_name = models.CharField(max_length=256, blank=False, verbose_name=_('First name'))
    last_name = models.CharField(max_length=256, blank=False, verbose_name=_('Last name'))
    middle_name = models.CharField(max_length=256, blank=True, verbose_name=_('Middle name'), default='')
    birthday = models.DateField(blank=False, verbose_name=_('Date of birth'), null=True)
    photo = models.ImageField(blank=True, verbose_name=_('Photo'), null=True)
    ticket = models.CharField(max_length=256, blank=False, verbose_name=_('Ticket'))
    notes = models.TextField(blank=True, verbose_name=_('Extra notes'))
    student_group = models.ForeignKey('Group', verbose_name=_('Group'), blank=False, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Group(models.Model):

    title = models.CharField(max_length=256, blank=False, verbose_name=_('Title'))
    leader = models.OneToOneField('Student', verbose_name=_('Leader'), blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name=_('Extra notes'))

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __str__(self):
        if self.leader:
            return '{}({} {})'.format(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '{}'.format(self.title)


class MonthJournal(models.Model):
    """
    Student monthly journal
    """
    class Meta:
        verbose_name = _('Month Journal')
        verbose_name_plural = _('Month Journals')

    student = models.ForeignKey('Student', verbose_name=_('Student'), blank=False, unique_for_month='date')
    date = models.DateField(verbose_name=_('Date'), blank=False)

    def __str__(self):
        return '{}: {}, {}'.format(self.student.last_name, self.date.month, self.date.year)

for i in range(1, 32):
    MonthJournal.add_to_class('present_day{}'.format(i), models.BooleanField(default=False))