from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='dhome'),
    path('about_us/', views.about, name="dabout"),
    path('services/',views.services, name='dservices'),
    path('healthCheck/', views.health, name="dhealth"),
    path('contact_us/', views.contact_us, name="dcontact_us"),
    path('map_show/', views.map_show, name="map_show"),
    path('profile/', views.profile, name="dprofile"),
    path('make_post/', views.make_post, name="makepost"),
    path('feed/', views.feed, name="feed")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)