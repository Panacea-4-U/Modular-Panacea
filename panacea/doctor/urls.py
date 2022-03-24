from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='dhome'),
    path('about_us/', views.about, name="dabout"),
    path('services/',views.services, name='dservices')
]