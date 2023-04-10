from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'smallblog/post_list.html', {'posts':posts})

def create_post(request):
    return render(request, 'smallblog/create_post.html')

def salve_post(request):
    title = request.POST.get('title')
    text = request.POST.get('text')

    post = Post(title=title, text=text)
    post.save()

    return redirect('post_list')

def edit_post(request, id_post):
    exist_post = Post.objects.get(pk=id_post)
    
    return render(request,'smallblog/edit_post.html',{'post':exist_post} )

def salve_edit(request, id_post):
    exist_post = Post.objects.get(pk=id_post)
    title = request.POST.get('title')
    text = request.POST.get('text')

    exist_post.text = text
    exist_post.title = title
    # falta implementar a vizualização de updated updated = timezone.now()

    exist_post.save()
    return redirect('post_list')

def delete_post(request, id_post):
    exist_post = Post.objects.get(pk=id_post)
    exist_post.delete()
    return redirect('post_list')


