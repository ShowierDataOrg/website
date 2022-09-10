from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
from . import admin 
from . import models
from . import forms
from django.template.exceptions import TemplateDoesNotExist 



def index(request):
    return render(request,'root.html')

def static(request:HttpResponse):
    try:
        return render(request,f"static/{request.GET.get('path', '')}")
    except (TemplateDoesNotExist , AttributeError,Exception) as e:
        return 404, (f"{request.GET.get('path', '')} does not exist") 

def contactme(request:HttpResponse):
    if request.POST:
        print(request.POST)
        r = dict(request.POST)
    
        form = forms.ContactForm(r)
        ctx = form.visible_fields()
        
        db = models.Contacted(
            
            r["subject"][0] ,
            r["message"][0],
            r["sender"][0],
           
        )
        
        db.save()
        return redirect('/')
    else:
        return render(request,'contactme.html')
        

# Create your views here.
