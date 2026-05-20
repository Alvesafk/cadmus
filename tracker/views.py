from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')

    if request.method == "POST":
        username = request.POST.get('username-input').strip()
        password = request.POST.get('password-input').strip()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'index.html', {'err': 'Usuário ou senha incorreto.'})
    return redirect('/')

@login_required(login_url="/")
def logout_user(request):
        logout(request)
        return redirect("/")

@login_required(login_url="/")
def dashboard(request):
    return render(request, "dashboard.html")
