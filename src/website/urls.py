from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('static',views.static),
    path('contact_us',views.contactme)
]
