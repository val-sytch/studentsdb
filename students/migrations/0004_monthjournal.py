# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('present_day1', models.BooleanField(default=False)),
                ('present_day2', models.BooleanField(default=False)),
                ('present_day3', models.BooleanField(default=False)),
                ('present_day4', models.BooleanField(default=False)),
                ('present_day5', models.BooleanField(default=False)),
                ('present_day6', models.BooleanField(default=False)),
                ('present_day7', models.BooleanField(default=False)),
                ('present_day8', models.BooleanField(default=False)),
                ('present_day9', models.BooleanField(default=False)),
                ('present_day10', models.BooleanField(default=False)),
                ('present_day11', models.BooleanField(default=False)),
                ('present_day12', models.BooleanField(default=False)),
                ('present_day13', models.BooleanField(default=False)),
                ('present_day14', models.BooleanField(default=False)),
                ('present_day15', models.BooleanField(default=False)),
                ('present_day16', models.BooleanField(default=False)),
                ('present_day17', models.BooleanField(default=False)),
                ('present_day18', models.BooleanField(default=False)),
                ('present_day19', models.BooleanField(default=False)),
                ('present_day20', models.BooleanField(default=False)),
                ('present_day21', models.BooleanField(default=False)),
                ('present_day22', models.BooleanField(default=False)),
                ('present_day23', models.BooleanField(default=False)),
                ('present_day24', models.BooleanField(default=False)),
                ('present_day25', models.BooleanField(default=False)),
                ('present_day26', models.BooleanField(default=False)),
                ('present_day27', models.BooleanField(default=False)),
                ('present_day28', models.BooleanField(default=False)),
                ('present_day29', models.BooleanField(default=False)),
                ('present_day30', models.BooleanField(default=False)),
                ('present_day31', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', unique_for_month='date', verbose_name='Студент')),
            ],
            options={
                'verbose_name_plural': 'Місячні Журнали',
                'verbose_name': 'Місячний Журнал',
            },
        ),
    ]
