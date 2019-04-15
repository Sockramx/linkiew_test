from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def videos(request):
    return render(request, 'lvideos/list.html')


