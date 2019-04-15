from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lvideos.forms import VideoModelForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def videos(request):
    
    titulo = 'list'
    form = VideoModelForm

    context = {
        'titulo': titulo,
        'form': form,
    }

    return render(request, 'lvideos/list.html', context)


