from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views import generic

# this one is for using django built in form
'''class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'''

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile:login')
    else:
        form = UserCreationForm()
    return render(request, 'profile/signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user = form.get_user()
            login(request, user)
            if 'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('site:home')
    else:
        form = AuthenticationForm()
    return render(request, 'profile/login.html', {'form': form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
    return redirect('site:home')
