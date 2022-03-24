from django.shortcuts import render
from panacea_app.models import Patient, TempDb, Doctor

# Create your views here.

def home(request, pk):
    context={'pk': pk}
    return render(request, 'patient/homepage.html', {'context': context})

def about(request, pk):
    context={'pk': pk}
    return render(request, 'patient/about_us.html', {'context': context})

def services(request, pk):
    data=Doctor.objects.all()
    context={'data': data, 'pk':pk}
    return render(request, 'patient/services.html',{'context': context})

def health(request, pk):
    print(request.method)
    if request.method == "POST":
        print(request.POST.get('gender'))
        print(request.POST.get('smoker'))
        print(request.POST.get('tobacco'))
        print(request.POST.get('bp'))
        print(request.POST.get('obese'))
        print(request.POST.get('diabetes'))
        print(request.POST.get('metabolic'))
        print(request.POST.get('stimulant'))
        print(request.POST.get('cardiac'))
        print(request.POST.get('preclam'))
        print(request.POST.get('cabg'))
        print(request.POST.get('respi'))
    context={'pk': pk}
    return render(request, 'patient/patientdetails.html', {'context': context})
