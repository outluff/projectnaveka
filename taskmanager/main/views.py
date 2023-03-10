from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def courses(request):
    return render(request, 'main/course.html')


def users(request):
    return render(request, 'main/user.html')


def accounts(request):
    return render(request, 'main/login.html')