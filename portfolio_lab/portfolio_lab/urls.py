"""portfolio_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from charitydonation.views import (LandingPageView, AddDonationView, LoginView, RegisterView, logout_view, UserPageView)
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', LandingPageView.as_view(), name='home'),
    path('add/', AddDonationView.as_view(), name='add'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name="logout"),
    path('user-page/', UserPageView.as_view(), name="user-page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
