from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password
import os
# Create your views here.
def RegistrationView(request):

    if request.method == 'POST':
        myuser = User()
        print(request.POST)
        myuser.first_name = request.POST.get('first_name')
        myuser.last_name = request.POST.get('last_name')
        myuser.gender = request.POST.get('gender')
        myuser.Hobbies = request.POST.getlist('Hobbies')
        myuser.email = request.POST.get('email')
        myuser.img = request.FILES.get('image')
        myuser.country = request.POST.get('country')
        myuser.password = make_password('password')
        print(myuser.Hobbies)
        myuser.save()
        return redirect('/employee/list')

    return render(request,'register.html',{'flag':True})
def employee_list(request):
    context = {'employee_list':User.objects.all()}
    return render(request,"employee_list.html",context)

def employee_delete(request,id):
    employee = User.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

def employee_update(request,id):

    employee = User.objects.get(pk=id)
    print(employee.Hobbies)

    if (request.method == 'POST'):

        if (request.FILES.get('image',None)):
            img = request.FILES['image'];
            employee.img = img
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.gender = request.POST.get('gender')
        employee.Hobbies = request.POST.getlist('Hobbies')

        employee.save()
        return redirect("/employee/list/")

    return render(request, "register.html",{'employee':employee})

def remove(request,id):
    employee = User.objects.get(pk=id)
    print('id')
    employee.img = ""
    employee.save()

    return render(request,"register.html",{'employee':employee})



