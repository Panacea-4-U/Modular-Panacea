from re import L
from django.shortcuts import render,redirect
from django.http import HttpResponse
from panacea_app.models import Patient, TempDb, Doctor
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic.list import ListView
from django.core.mail import send_mail
from random import randint
from django.db.models import Q
from patient import views as pviews
from doctor import views as dviews

# Create your views here.

def home(request):
    return render(request,'panacea_app/homepage.html')

def landingpage(request):
    return render(request,'panacea_app/landingpage.html')

def login_register(request):
    if(request.method == "POST" and request.POST.get('register')=="register"):
        pd_id=randint(1000000000,9999999999)
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpass = request.POST.get("con_password")
        category = request.POST.get("category")
        lic_no = randint(1000000000,9999999999)
        if( password == confpass ):
            if (category == "patient"):
                patient = Patient()
                patient.pat_id=pd_id
                patient.name = name
                patient.email = email
                patient.password = password
                patient.save()
                return redirect(pviews.home, pk=pd_id)
            elif (category == "doctor"):
                doctor = Doctor()
                doctor.doc_id=pd_id
                doctor.name = name
                doctor.email = email
                doctor.password = password
                doctor.licence_no = lic_no
                doctor.save()
                return redirect(dviews.home, pk=pd_id)
    elif(request.method == "POST" and request.POST.get('login')=="login"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(email,password)
        doctor=None
        patient=None
        try:
            doctor=Doctor.objects.get(email=email)
        except:
            try:
                patient=Patient.objects.get(email=email)
            except:
                return render(request,'panacea_app/login_register.html')
        if(doctor!=None):
            if(doctor.password==password):
                return redirect(dviews.home, pk=doctor.doc_id)
        if(patient!=None):
            if(patient.password==password):
                return redirect(pviews.home, pk=patient.pat_id)
    return render(request,'panacea_app/login_register.html')

def doctordetails(request):
    return render(request,'panacea_app/doctordetails.html')

def patientdetails(request):
    return render(request,'panacea_app/patientdetails.html')

def contact_us(request):
    if(request.method=="POST"):
        name=request.POST.get('firstname')
        rec_email=request.POST.get('email')
        subject = request.POST.get('subject')
        message = f'Hi {name}, thank you for contacting Panacea our agents will get in touch with you soon...'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [rec_email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(request, 'panacea_app/contact_us.html')
		
def about_us(request):
    return render(request, 'panacea_app/about_us.html')
    
def check(request):
    if(request.method=="POST"):
        temp=TempDb()
        temp.name=request.POST.get('name')
        temp.email=request.POST.get('email')
        temp.ph_no=request.POST.get('ph_no')
        temp.save()
        return redirect('/')
    return render(request,'panacea_app/check.html')

def pat_home(request,pk):
    return render(request,'panacea_app/patienthome.html')


class SearchView(ListView):
	model = Doctor
	template_name = 'panacea_app/services.html'
	context_object_name = 'all_search_results'
	print("Checking")
	def get_queryset(self):
		result = super(SearchView, self).get_queryset()
		query = self.request.GET.get('search')
		print(query)
		if query:
			postresult = Doctor.objects.filter(
				Q(name__contains=query) | Q(email__contains=query)
			)
			result = postresult
		else:
			result = Doctor.objects.all()
		return result