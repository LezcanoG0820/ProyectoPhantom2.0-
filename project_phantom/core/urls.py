"""
URL configuration for project_phantom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views, exit
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.home, name="home"), #Se esta importando la vista "home.html" y lo que hay dentro de ella.
    path("products/", views.products, name="products"), #Se esta importando la vista "products.html" y todo lo que este dentro de esta
    path('accounts/login/', LoginView.as_view(), name='login'),
    path("logout/", views.logout_view, name="logout"),
]



