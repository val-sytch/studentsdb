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

