from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='phome'),
    path('about_us/', views.about, name="pabout"), 
    path('services/', views.services, name="pservices"),
    path('healthCheck/', views.health, name="phealth"),
    path('contact_us/', views.contact_us, name="pcontact_us"),
    path('map_show', views.map_show, name="map_show"),
    path('profile/', views.profile, name="pprofile"),
    path('feed/', views.pfeed, name="pfeed"),
    path('doctors_details/<int:pk2>/', views.dpdetails, name="dpdetails"),
    path('bookmark/<int:pk3>/', views.bookmark, name="bookmark"),
    path('pat_bookmark', views.pat_bookmark, name="pat_bookmark")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)