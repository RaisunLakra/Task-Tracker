from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as UserLogin, logout as UserLogout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                username = form.cleaned_data.get('username')
                # print("singup successfull")
                messages.success(request, f'Account for {username} is created.')
                return redirect('authentication:login')
        else:
            # print("form is not valid")
            return render(request, 'signup.html', {'form': form})
        
    else :
        form = UserCreationForm()
        return render(request,'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        # print('Post method called')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # print('form is valid')
            UserLogin(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('app:tasks')
        else:
            # print('wrong id or password')
            messages.error(request, 'Login failed. Please check your credentials.')
            return redirect('authentication:login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
def logout(request):
    UserLogout(request)
    messages.success(request, 'You are logged out')
    return redirect('authentication:login')