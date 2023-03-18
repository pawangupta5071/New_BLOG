from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Post, Comment
from .forms import PostForm
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.



def home(request):
    posts=Post.objects.all()
    myFilter=PostFilter(request.GET,queryset=posts)
    posts=myFilter.qs

    page=request.GET.get('page')
    paginator = Paginator(posts,3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts =paginator.page(1)
    except EmptyPage:
        posts =paginator.page(paginator.num_pages)

    context={"posts": posts,"myFilter": myFilter}
    return render(request, 'base/home.html',context)

def post_detail(request,slug):
    posts=Post.objects.filter(active=True,featured=True)[0:3]
    post_detail = Post.objects.get(slug=slug)
    context={"post_detail": post_detail,"posts":posts}
    return render(request,"base/post_detail.html",context)

def about_us(request):
    posts=Post.objects.filter(active=True,featured=True)[0:3]
    context={"posts":posts}
    return render(request,"base/about_us.html",context)

def contact_us(request):
    return render(request,"base/contact_us.html")


# CRUD VIEWS

def create_post(request):
    form = PostForm(request.POST)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request,"base/post_form.html",context)

def update_post(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request,"base/post_form.html",context)

def delete_post(request,slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'item': post}
    return render(request,"base/post_delete.html",context)


# Send Email view

def send_email(request):
    if request.method == "POST":
        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(request.POST['subject'],template,settings.EMAIL_HOST_USER,['pkgupta5071453@gmail.com'])
        email.fail_silently=False
        email.send()
    return render(request,'base/email_send.html')