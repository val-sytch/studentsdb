# -*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=256, blank=False, verbose_name='Ім’я')
    last_name = models.CharField(max_length=256, blank=False, verbose_name='Прізвище')
    middle_name = models.CharField(max_length=256, blank=True, verbose_name='По - батькові', default='')
    birthday = models.DateField(blank=False, verbose_name='Дата народження', null=True)
    photo = models.ImageField(blank=True, verbose_name='Фото', null=True)
    ticket = models.CharField(max_length=256, blank=False, verbose_name='Білет')
    notes = models.TextField(blank=True, verbose_name='Додаткові нотатки')
    student_group = models.ForeignKey('Group', verbose_name='Група', blank=False, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Group(models.Model):

    title = models.CharField(max_length=256, blank=False, verbose_name='Назва')
    leader = models.OneToOneField('Student', verbose_name='Староста', blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name='Додаткові нотатки')

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

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
        verbose_name = 'Місячний Журнал'
        verbose_name_plural = 'Місячні Журнали'

    student = models.ForeignKey('Student', verbose_name='Студент', blank=False, unique_for_month='date')
    date = models.DateField(verbose_name='Дата', blank=False)

    def __str__(self):
        return '{}: {}, {}'.format(self.student.last_name, self.date.month, self.date.year)

for i in range(1, 32):
    MonthJournal.add_to_class('present_day{}'.format(i), models.BooleanField(default=False))