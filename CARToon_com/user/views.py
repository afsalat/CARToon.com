from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Endpoint: user login
def login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                return render(request, 'Login.html', {'error': 'Invalid username or password'})
                            
        return render(request, 'Login.html')

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
        redirect("Login")

        return redirect(request, "Login")


    except Exception as e:
        return render(request, "Home.html", {"message":str(e), "status_code":500})
