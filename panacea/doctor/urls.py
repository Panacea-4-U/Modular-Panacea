from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='dhome'),
    path('about_us/', views.about, name="dabout"),
    path('services/',views.services, name='dservices'),
    path('healthCheck/', views.health, name="dhealth"),
    path('contact_us/', views.contact_us, name="dcontact_us"),
    path('map_show', views.map_show, name="map_show")
]