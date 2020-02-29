from django.views import View
from django.shortcuts import render, redirect
from django.contrib import auth

from ..forms import LoginForm, RegistrationForm
from ..forms.util import BootstrapErrors

class Login(View):
    def get(self, request):
        return render(request, "auth/login.html", {"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST, label_suffix="")
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is None:
                return render(request, "auth/login.html", {"form": form, "base_error": "Username or password is invalid."})
            else:
                auth.login(request, user)
                if not "remember" in form:
                    request.session.set_expiry(0)
                return redirect("/dashboard")
        else:
            return render(request, "auth/login.html", {"form": form})

class Register(View):
    def get(self, request):
        return render(request, "auth/register.html", {"form": RegistrationForm()})
