from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Category
from categorys.forms import CategoryModelForm

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def list(request):
    title = 'Categories'
    obj = Category.objects.filter()

    context = {
        'title': title,
        'obj': obj,
    }
    return render(request, 'categorys/list.html', context)


@login_required(login_url='login')
def create(request):
    title = 'Create'

    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item created success')
            return redirect('categorys:list')
        else:
            messages.success(request, 'Error, item no save')
    else:
        form = CategoryModelForm()
        
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'categorys/create.html', context)


@login_required(login_url='login')
def edit(request, id):
    title = 'Edit'
    instance = Category.objects.get(id=id)
    form = CategoryModelForm(request.POST or None, instance=instance)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Item update success')
        return redirect('categorys:list')
    else:
        messages.success(request, 'Item no save')

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'categorys/edit.html', context)


@login_required(login_url='login')
def delete(request, id):
    title = 'Delete'
    instance = Category.objects.get(id=id)
    instance.delete()
    messages.warning(request, 'Message delete success')
    
    context = {
        'title': title,
    }
    return render(request, 'categorys/delete.html', context)