from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='phome'),
    path('about_us/', views.about, name="pabout"), 
    path('services/', views.services, name="pservices"),
    path('healthCheck/', views.health, name="phealth"),
    path('contact_us/', views.contact_us, name="pcontact_us")
]