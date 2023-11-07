from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'login.html', {'error_message': 'Неправильное имя пользователя или пароль.'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return login_view(request)

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Проверяем, существует ли пользователь с таким именем
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error_message': 'Пользователь с таким именем уже существует.'})
            else:
                # Создаем нового пользователя
                user = User.objects.create(username=username, password=password)
                user.save()
                return redirect('login')  # Перенаправляем на страницу входа
        else:
            return render(request, 'register.html', {'error_message': 'Пароли не совпадают.'})

    return render(request, 'register.html')

