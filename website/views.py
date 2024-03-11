from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from . import models
from django.contrib import messages


def registration_page(request):
    form = models.RegisterForm()
    context = {'form': form}
    if request.method == "POST":
        form = models.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(request, "User Creation Failed. Try again!")
    return render(request, 'register_page.html', context)


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
    if request.method == "POST":
        data = models.Students()
        data.s_name = request.POST.get('s_name')
        data.s_email = request.POST.get('email')
        data.s_phone = request.POST.get('phone')
        try:
            if data != "":
                data.save()
                messages.success(request, 'Entry created successfully!')
        except (TypeError, ValueError):
            messages.error(request, 'Incomplete Data!')

    r_data = models.Students.manager.all()
    context = {'r_data': r_data}
    return render(request, 'dashboard.html', context)


def update_student(request, pk):
    data = models.Students.manager.get(pk=pk)
    context = {'data': data}
    if request.method == "POST":
        data.s_name = request.POST.get("name")
        data.s_email = request.POST.get("email")
        data.s_phone = request.POST.get("phone")
        data.save()
        messages.success(request, "Student details updated successfully.")
    return render(request, 'update.html', context)


def delete_student(request, id):
    data = models.Students.manager.filter(pk=id)
    context = {'data': data}
    return render(request, 'delete.html', context)
