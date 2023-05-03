from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .form import RegisterForm,LoginForm
# Create your views here.

def index (request):
    return render (request, 'account/index.html')

def register(request):
    
    form = RegisterForm()
    context = {'form':form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    return render(request, 'account/register.html', context)

def Login_user(request):
    form = LoginForm()
    context = {'form':form}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(index)
    return render (request, 'account/login.html', context)