from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from charitydonation.models import Category, Institution, Donation
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        all_donations = Donation.objects.all()
        institutions = Institution.objects.all()
        fundacje = Institution.objects.filter(type='F')
        organizacje_pozarządowe = Institution.objects.filter(type='OPZ')
        zbiórki_lokalne = Institution.objects.filter(type='ZL')
        donations = 0
        # - dodaj liczenie worków
        for donation in all_donations:
            donations = donations + donation.quantity
        # - dodaj liczenie wspartych organizacji
        how_many_institutions = len(institutions)
        ctx = {'donations': donations, 'how_many_institutions': how_many_institutions, 'fundacje': fundacje,
               'organizacje_pozarządowe': organizacje_pozarządowe, 'zbiórki_lokalne': zbiórki_lokalne}

        response = render(request, 'index.html', ctx)
        return response


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        ctx = {'categories': categories, 'institutions': institutions}
        response = render(request, 'form.html', ctx)
        return response


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        username = email
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Zalogowano!")
            return redirect("home")
        else:
            if not User.objects.filter(email=email).exists():
                return redirect("register")
            else:
                messages.error(request, "Błąd w nazwie użytkownika lub haśle")
                return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        response = render(request, 'register.html')
        return response

    def post(self, request):
        password = request.POST.get("password")
        if (request.POST.get("name") and request.POST.get("surname") and request.POST.get("email") and request.POST.get(
                "password")):
            if (request.POST.get("password") == request.POST.get("password2")):
                new_user = User.objects.create(first_name=request.POST.get("name"),
                                               last_name=request.POST.get("surname"), email=request.POST.get("email"),
                                               username=request.POST.get("email"))
                new_user.set_password(password)
                new_user.save()

        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect("home")


class UserPageView(View):
    def get(self, request):
        response = render(request, 'user-page.html')
        # ile worków zostało przekazane,
        # jakiej organizacji
        # z jakich kategorii
        # oraz kiedy zostały / będą zabrane
        return response