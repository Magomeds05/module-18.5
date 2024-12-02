from django.shortcuts import render
from django.shortcuts import HttpResponse
from task5.forms import UserRegister

def sign_up_by_html(request):
    users = ['Nikita', 'Magomed', 'Ruslan']
    info = {}
    context = {'info': info}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветсвуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    users = ['Nikita', 'Magomed', 'Ruslan']
    info = {}
    context = {'info': info}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветсвуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', context)


# Create your views here.
