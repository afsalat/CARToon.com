from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



# Endpoint: user login
def login(request):
    try:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():

                user = form.get_user()
                login(request, user)  

                print("User authenticated and logged in!")  

                return redirect('home') 
            else:
                print("Form is not valid")
                print(form.errors)  
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
        print(request.user)
        logout(request)
        request.session.flush()
        return redirect("Login")

    except Exception as e:
        return render(request, "Home.html", {"message":str(e), "status_code":500})
