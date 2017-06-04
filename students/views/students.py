from django.shortcuts import render


def students_list(request):
    context = {'students':
        ({'id': 1, 'first_name': 'Віталій','last_name': 'Подоба','ticket': 235,'image': 'img/me.jpeg'},
        {'id': 2,'first_name': 'Корост','last_name': 'Андрій','ticket': 2123,'image': 'img/piv.png'})
               }

    return render(request, 'students/students_list.html', context)


def student_add(request):
    pass


def student_edit(request):
    pass


def student_delete(request):
    pass