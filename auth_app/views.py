from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            
            login_url = reverse('auth_app:login')  # Replace 'auth_app' with your app's name (make redirec dynamic)
            return redirect(login_url)
    return render(request,'user/Login.html')
    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        c_password = request.POST['password2']
        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username is already taken')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'E-mail is already taken')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print('user is created...')
                return render(request,'user/successfullREG.html',{'username':username})
                
        else:
            messages.info(request,'Pssword is no\'t match')
            register_url = reverse('auth_app:register')  # Replace 'auth_app' with your app's name (make redirec dynamic)
        return redirect(register_url)
    return render(request,'user/Registration.html')

from . forms import CustomUserChangeForm

# def edit_profile(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('/profile/')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'user/editProfile.html', {'form': form})

from django.contrib.auth import update_session_auth_hash

def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout

            profile_url = reverse('projectApp:profile')  # Replace 'auth_app' with your app's name (make redirec dynamic)
            return redirect(profile_url)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'user/editProfile.html', {'form': form})




def logout(request):
    auth.logout(request)
    return redirect('/')