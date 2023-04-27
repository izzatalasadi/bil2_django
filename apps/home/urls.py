
from django.urls import path, re_path

from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path("contact/", views.contactView, name="contact"),
    path("success/", views.successView, name="success"),
    path("buy/", views.buyView, name="buy"),
    path("sell/", views.sellView, name="sell"),
    path("about/", views.aboutView, name="about"),
    path("service/", views.serviceView, name="services"),
    
    re_path(r'^.*\.*', views.pages, name='pages'),

]
