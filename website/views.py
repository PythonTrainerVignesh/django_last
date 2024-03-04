from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def home(request):
    context = {}  # logic/data
    return render(request, 'index.html', context)


def login_page(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard.html')


def registration_page(request):
    return render(request, 'register_page.html')
