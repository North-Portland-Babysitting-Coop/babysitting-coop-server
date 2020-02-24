from django.views import View
from django.shortcuts import render

from ..forms import LoginForm

class Login(View):
    def get(self, request):
        return render(request, "auth/login.html", {"form": LoginForm()})
