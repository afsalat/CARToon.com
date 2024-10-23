from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm



# Endpoint: user login
def login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            
            auth_user = authenticate(request , username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('Home')
            
        return render(request, 'Login.html')

    except Exception as e:
        return response({"message":str(e), "status_code":500})


#Endpoint: user register
def Register(request):
    try:
        if request.method == "POST":
            new_user = UserCreationForm(request.POST)
            
            if new_user.is_valid():
                new_user.save()
                return redirect('Login')
            
        else:
            new_user = UserCreationForm()

        return render(request, 'Register.html', {"new_user":new_user})

    except Exception as e:
        return response({"message":str(e), "status_code":500})


#Endpoint: user logout
def logout(request):
    try:
        logout(request)
        redirect('Login')

    except Exception as e:
        return response({"message":str(e), "status_code":500})
