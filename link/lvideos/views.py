from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Video
from lvideos.forms import VideoModelForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def list(request):
    title = 'List'
    obj = Video.objects.filter(user=request.user)

    context = {
        'title': title,
         'obj': obj,
    }
    return render(request, 'lvideos/list.html', context)


@login_required(login_url='login')
def create(request):
    title = 'Create'

    if request.method == 'POST':
        form = VideoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item created success')
            return redirect('videos:list')    
        else:
            messages.success(request, 'Error, item no save')
    else:
        form = VideoModelForm()
        
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'lvideos/create.html', context)


@login_required(login_url='login')
def edit(request, video_id):
    title = 'Edit'
    instance = Video.objects.get(id=video_id)
    form = VideoModelForm(request.POST or None, instance=instance)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Item update success')
        return redirect('videos:list')
    else:
        messages.success(request, 'Item no save')


    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'lvideos/edit.html', context)


@login_required(login_url='login')
def delete(request, video_id):
    title = 'Delete'
    instance = Video.objects.get(id=video_id)
    instance.delete()
    messages.warning(request, 'Message delete success')
    
    context = {
        'title': title,
    }
    return render(request, 'lvideos/delete.html', context)   