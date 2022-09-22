from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def settings(request):
    return render(request, 'setting.html')


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('signup')
            else:
                user =  User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                # login the user and redirect to settings page.
                user_login = authenticate(username=username, password=password)
                login(request, user_login)

                # linking to the Profile model.
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, userId=user_model.id)
                new_profile.save()

                return redirect('settings')
        else:
            messages.info(request, "Passsword doesn't match!")
            return redirect('signup')
        

    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout_view(request):
    logout(request)
    return redirect('signin')



