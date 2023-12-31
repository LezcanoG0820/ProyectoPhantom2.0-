from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.


def home(request):
    return render(request, "home.html")

@login_required
def products(request):
    return render(request, "products.html")

def logout_view(request):
    logout(request)
    return redirect("home")
