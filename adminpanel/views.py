from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
# ===========================================================================================
# ================================Admin-Login===================================================

@csrf_exempt
def adminlogin(request):
    if request.session.has_key('key'):
        return redirect('adminhome')
    else:
        if request.method == 'POST':
            username = request.POST['name1']
            password = request.POST['pass1']
            if username == 'admin' and password == '123':
                request.session['key'] = 'seceret1'
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return render(request, 'admin/ad-login.html')


# ===========================================================================================
# ================================Admin-Login===================================================
def adminhome(request):
    if request.session.has_key('key'):
        users = User.objects.all()
        context = {
            'users': users, 
        }
        return render(request, 'admin/ad-home.html', context)
    else:
        return redirect('adminlogin')    


# ===========================================================================================
# ================================Admin-Create user===================================================
@csrf_exempt
def adminadd(request):
    if request.session.has_key('key'):
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
            return redirect('adminhome')
    else:
        return redirect('adminlogin')      

        

# ===========================================================================================
# ================================Admin-Update===================================================
@csrf_exempt
def adminupdate(request, pk):
    if request.session.has_key('key'):
        update = User.objects.get(id=pk)
        if request.method == 'POST':
            update.firstname = request.POST['fname1']
            update.lastname = request.POST['lname1']
            update.username = request.POST['uname1']
            update.email = request.POST['email1']
            if User.objects.filter(username=update.username).exclude(id=pk).exists():
                print('username is already taken')
                return JsonResponse('false1', safe=False)
            elif User.objects.filter(email=update.email).exclude(id=pk).exists():
                print('email is already taken')
                return JsonResponse('false2', safe=False)

            else:
                update.save()         
                print('user is update')
                return JsonResponse('true', safe=False)
        else:
            # update = User.objects.get(id=pk)
            context = {
                'update': update
            }
            return render(request, 'admin/ad-update.html', context)
    else:
        return redirect('adminlogin')


#===================================================================================
# ================================Admin-Delete===================================================
def admindelete(request, pk):
    if request.session.has_key('key'):
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('adminhome')
    else:
        return redirect('adminlogin')



# ===========================================================================================
# ================================Admin-Search===================================================
def adminsearch(request):
    if request.session.has_key('key'):
        if 'q' in request.GET:
            q = request.GET['q']
            users = User.objects.filter(username__icontains= q)
            print(users)
        else:    
            users = User.objects.all()
    
        return render(request, 'admin/search.html', {'users':users})
    else:
        return redirect('adminlogin')
# ===========================================================================================
# ================================Admin-Logout===================================================
def adminlogout(request):
    request.session.flush()
    return redirect('adminlogin')


