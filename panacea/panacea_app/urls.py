from django.urls import include, path
from . import views
from doctor import views as dviews
from patient import views as pviews

urlpatterns = [
    path('', views.home,name='web-home'),
    path('doctor/<int:pk>/', include('doctor.urls')),
    path('patient/<int:pk>/', include('patient.urls')),
    path('patient/<int:pk>/',views.pat_home,name='pat-home'),
    path('landing', views.landingpage,name='landing-page'),
    path('login-register', views.login_register,name='login-register'),
    path('about_us',views.about_us,name='about us'),
    path('contact_us',views.contact_us,name='contact us'),
    path('doctor-details', views.doctordetails,name='doctordetails'),
    path('patient-details', views.patientdetails,name='patientdetails'),
    path('db_check/',views.check, name='check'),
    path('services/',views.SearchView.as_view(), name='services'),
    path('map_show', views.map_show, name="map_show")
]


'''

path('patient/<int:pk>/',views.pat_home,name='pat-home'),
    path('landing', views.landingpage,name='landing-page'),
    path('login-register', views.login_register,name='login-register'),
    path('about_us',views.about_us,name='about us'),
    path('contact_us',views.contact_us,name='contact us'),
    path('doctor-details', views.doctordetails,name='doctordetails'),
    path('patient-details', views.patientdetails,name='patientdetails'),
    path('db_check/',views.check, name='check'),
    path('services/',views.SearchView.as_view(), name='services')'''