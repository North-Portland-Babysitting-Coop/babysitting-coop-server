from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html', {"user": request.user})
