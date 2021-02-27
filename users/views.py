from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Register(request):
    if request.method == 'POST' :   
        form = UserRegisterForm(request.POST)
        form.save()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has being created! You are now able to log in')
        return redirect('login')

    else:       
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form })

@login_required
def Profile(request):
    return render(request,'users/Profile.html')
