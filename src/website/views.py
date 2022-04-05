from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'root.html')

def static(request):
    return render(request,f"static/{request.GET.get('path', '')}")