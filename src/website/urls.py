from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('static',views.static),
    path('about',views.about_me),
    path('contact_us',views.contactme)
]