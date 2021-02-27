from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http  import JsonResponse,response
from django.views.decorators.csrf import csrf_exempt

 


# Create your views here.
# ===========================================================================================
# ================================Register===================================================
@csrf_exempt
def register(request):
    if request.method == 'POST':
        firstname = request.POST['fname1']
        lastname = request.POST['lname1']
        username = request.POST['uname1']
        email = request.POST['email1']
        password1 = request.POST['pass_1']
        if User.objects.filter(username=username).exists():
            print('username is already taken')
            return JsonResponse('false1', safe=False)
        elif User.objects.filter(email=email).exists():
            print('email is already taken')
            return JsonResponse('false2', safe=False)

        else:
            user =  User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password1)
            
            print('user is created')
            return JsonResponse('true', safe=False) 
    else:
        return render(request, 'myapp/signup.html')      
    return render(request, 'myapp/signup.html')

# ===========================================================================================
# ================================Login===================================================
@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['name1']
            password = request.POST['pass1']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print('go to home')
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
                print("incorrect username or password")
                return JsonResponse('false', safe=False)
        else:
            return render(request, 'myapp/login.html')


# ===========================================================================================
# ================================Home===================================================

def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return redirect('login')

# ===========================================================================================
# ================================Logout===================================================

def userlogout(request):
    request.session.flush()
    logout(request)
    return redirect('login')

