from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from .models import User
from blog.models import Post,Category
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if request.FILES.get('image') == None:
            messages.info(request,'please upload a image ')
        if request.FILES.get('image') != None:
            profileimg =request.FILES.get('image') 
        first_name=request.POST['firstname'] 
        last_name=request.POST['lastname']
        Area=request.POST['Area']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        patient=request.POST['patient']
        doctor=request.POST['doctor']
        if patient == '' and doctor == '':
            messages.info(request,'you should enter P or D dont leave these sections empty')
            return redirect('account:register')
       




        if password != password2:
            messages.info(request,'both passwords are not matching')
            return redirect('account:register')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken') 
                return redirect('account:register') 
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken') 
                return redirect('account:register') 
           

            else:
                
                if doctor == 'D':
                    
                    user = User.objects.create_user(username=username,email=email,password=password,profileimg=profileimg,first_name=first_name,last_name=last_name,
                Area=Area,city=city,state=state,pincode=pincode,is_Patient=patient,is_Doctor=doctor,is_staff=True
                )
                    user.save()
                
                if patient =='P':
                    
                    user = User.objects.create_user(username=username,email=email,password=password,profileimg=profileimg,first_name=first_name,last_name=last_name,
                Area=Area,city=city,state=state,pincode=pincode,is_Patient=patient,is_Doctor=doctor
                )    
                    user.save()

                
                return redirect('account:login_view')



    else:
       return render(request,'register.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None



    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_Patient=='P':
                user.save()
                login(request, user)
                return redirect('account:patient')
            elif user is not None and user.is_Doctor=='D':
                user.save()
                login(request, user)
                return redirect('account:doctor')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
            
    return render(request, 'login.html', {'form': form, 'msg': msg})




def patient(request):
    return render(request,'patient.html')


def doctor(request):
    return render(request,'doctor.html')

@login_required(login_url='account:login_view')
def logout(request):
    auth.logout(request)
    return redirect('account:login_view')
