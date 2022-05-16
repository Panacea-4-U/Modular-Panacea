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
    path('feed/', views.feed, name="feed"),
    path('add_address/', views.add_address, name="add_address"),
    path('add_speciality/', views.add_speciality, name="add_speciality"),
    path('remove_address/', views.remove_address, name="remove_address"),
    path('update_doc', views.update_doc, name="update_doc"),
    path('doctors_det/<int:pk2>/', views.dpdetails2, name="dpdetails2"),
    path('bookmark/<int:pk3>/', views.bookmark, name="bookmark"),
    path('doc_bookmark', views.doc_bookmark, name="doc_bookmark")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)