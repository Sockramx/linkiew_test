from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Video
from lvideos.forms import VideoModelForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def list(request):
    title = 'List'
    obj = Video.objects.all()

    context = {
        'title': title,
         'obj': obj,
    }
    return render(request, 'lvideos/list.html', context)


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = VideoModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('videos:list')    
    else:
        form = VideoModelForm()

    title = 'Create'
    
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'lvideos/create.html', context)


@login_required(login_url='login')
def edit(request, video_id):
    print('zzzz')
    print(video_id)
    title = 'Edit'

    context = {
        'title': title,
    }
    return render(request, 'lvideos/edit.html', context)


@login_required(login_url='login')
def delete(request):
    title = 'Delete'

    context = {
        'title': title,
    }
    return render(request, 'lvideos/delete.html', context)   