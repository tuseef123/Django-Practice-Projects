from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm,LoginForm
from django.contrib import messages
from .models import Post
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
            form.save()
    else:
        form = SignupForm()
    return render(request,'blog/signup.html',{'form':form})
