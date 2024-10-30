from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import login as login_view
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# Endpoint: user login
def login(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                print("--",user)
                if user is not None:
                    login_view(request, user)
                    return redirect('Home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    except Exception as e:
        return render(request, 'Login.html', {"message":str(e), "status_code":500})


#Endpoint: user register
def Register(request):
    try:

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('Login')
            
        else:
            form = UserCreationForm()

        return render(request, 'Register.html', {"form":form})

    except Exception as e:
        return render(request, 'Register.html', {"message":str(e), "status_code":500})


#Endpoint: user logout
def logout(request):
    try:
        logout(request)
        request.session.flush()
        return redirect("Login")

    except Exception as e:
        return render(request, "Home.html", {"message":str(e), "status_code":500})
