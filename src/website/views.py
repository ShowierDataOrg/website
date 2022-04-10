from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
from . import admin as models
from . import forms
from django.template.exceptions import TemplateDoesNotExist 



def index(request):
    return render(request,'root.html')

def static(request:HttpResponse):
    try:
        return render(request,f"static/{request.GET.get('path', '')}")
    except (TemplateDoesNotExist , AttributeError,Exception) as e:
        return 404, (f"{request.GET.get('path', '')} does not exist") 
def about_me(request:HttpResponse):
    return render(request,'about.html')
def contactme(request:HttpResponse):
    if request.POST:
        print(request.POST)
        r = dict(request.POST)
    
        form = forms.ContactForm(r)
        ctx = form.visible_fields()
        db = models.Contacted
        db.objects.create(
            uuid = uuid.uuid4(),
            subject =ctx['1'] ,
            message=ctx[2],
            sender=ctx[3]
        )
        
        db.save()
        return redirect('/')
    else:
        return render(request,'contactme.html')
        

# Create your views here.
