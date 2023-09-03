from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# def LoginView(request):
#     return render(request, 'login.html')

@login_required
def dash(request):
    return render(request, 'dash.html')


def page_one(request):
    return render(request, 'page_one.html')


def page_two(request):
    return render(request, 'page_two.html')


def login_view(request):
    print("heloooooooo")
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        print("helooo")
        if user is not None:
            login(request, user)
            print("helloooo")
            if user.is_staff:
                print("hellooooooo")
                return redirect('dash')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')
