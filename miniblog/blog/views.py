from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

# Home page
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

# Contact
def contact(request):
    return render(request,'blog/contact.html')

# About
def about(request):
    return render(request,'blog/about.html')

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!! ')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

# Signup
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrates you have become an author')

            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignupForm()
    return render(request,'blog/signup.html',{'form':form})
# Add New Post

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                messages.success(request,'Post Added Successfully!!')
                pst.save()
                return HttpResponseRedirect('/addpost/')
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
# Update Posts
def update_post(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=pk)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,'Post Updates successfully!!')
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=pk)
            form = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
# Delete Posts
def delete_post(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=pk)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# 404 ERROR 

def handler404(request,exception):
    return render(request,'blog/404.html')