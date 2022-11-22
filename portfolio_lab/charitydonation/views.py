from django.shortcuts import render
from django.views import View
from charitydonation.models import Category, Institution, Donation


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        all_donations = Donation.objects.all()
        institutions = Institution.objects.all()
        donations = 0
        # - dodaj liczenie worków
        for donation in all_donations:
            donations = donations + donation.quantity
        # - dodaj liczenie wspartych organizacji
        how_many_institutions = len(institutions)
        ctx = {'donations': donations, 'how_many_institutions': how_many_institutions, 'institutions': institutions}

        response = render(request, 'index.html', ctx)
        return response


class AddDonationView(View):
    def get(self, request):
        response = render(request, 'form.html')
        return response


class LoginView(View):
    def get(self, request):
        response = render(request, 'login.html')
        return response


class RegisterView(View):
    def get(self, request):
        response = render(request, 'register.html')
        return response
