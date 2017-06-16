import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from students.models import Student, Group, MonthJournal


@receiver([post_save, post_delete], sender=Student)
def log_student_crud(sender, **kwargs):
    """
    Log information about student into log file
    """
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    created = kwargs.get('created')

    if created is None:
        message = "Student deleted: %s %s (ID: %d)"
    elif created:
        message = "Student added: %s %s (ID: %d)"
    else:
        message = "Student updated: %s %s (ID: %d)"
    logger.info(message, student.first_name, student.last_name, student.id)


@receiver([post_save, post_delete], sender=Group)
def log_group_crud(sender, **kwargs):
    """
    Log information about group into log file
    """
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    created = kwargs.get('created')

    if created is None:
        message = "Group deleted: %s (ID: %d)"
    elif created:
        message = "Group added: %s (ID: %d)"
    else:
        message = "Group updated: %s (ID: %d)"
    logger.info(message, group.title, group.id)


@receiver([post_save, post_delete], sender=MonthJournal)
def log_month_journal_crud(sender, **kwargs):
    """
    Log information about month journal into log file
    """
    logger = logging.getLogger(__name__)

    month_journal = kwargs['instance']
    created = kwargs.get('created')
    print(kwargs)
    if created is None:
        message = "Month journal for student %s %s for date %s %s deleted: (ID: %d)"
    elif created:
        message = "Month journal for student %s %s for date %s %s added: (ID: %d)"
    else:
        message = "Month journal for student %s %s for date %s %s updated: (ID: %d)"
    logger.info(message, month_journal.student.first_name, month_journal.student.last_name,
                month_journal.date.month, month_journal.date.year, month_journal.id)


