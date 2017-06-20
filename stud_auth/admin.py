from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User
from stud_auth.models import StudentProfile


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile


class UserAdmin(auth_admin.UserAdmin):
    inlines = (StudentProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
