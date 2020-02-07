from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    html = "<html><body>It is now WHAT UP BITCHES.</body></html>"
    return HttpResponse(html)
