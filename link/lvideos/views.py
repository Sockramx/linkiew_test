from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lvideos.forms import VideoModelForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def list(request):
    title = 'List'
    
    context = {
        'title': title,
    }
    return render(request, 'lvideos/list.html', context)


def create(request):
    title = 'Create'
    form = VideoModelForm

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'lvideos/create.html', context)


def edit(request):
    title = 'Edit'

    context = {
        'title': title,
    }
    return render(request, 'lvideos/edit.html', context)


def delete(request):
    title = 'Delete'

    context = {
        'title': title,
    }
    return render(request, 'lvideos/delete.html', context)   