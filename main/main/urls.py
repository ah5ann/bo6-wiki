"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import login_view

urlpatterns = [
    path("accounts/login/", login_view, name='login'),  # Custom login view
    path("accounts/", include("django.contrib.auth.urls")),  # This includes the default auth URLs
    path("", include('class_upvote.urls')),  # Include your app URLs
    path("", views.home, name="Home"),  # Home view
    path('admin/', admin.site.urls),  # Admin interface
]
