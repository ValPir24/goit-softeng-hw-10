from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Отримати пароль, якщо потрібно
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})
