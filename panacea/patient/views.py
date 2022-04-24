from django.shortcuts import render
from panacea_app.models import Patient, TempDb, Doctor
from doctor.models import PostDb

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

def contact_us(request,pk):
    context={'pk': pk}
    patient=Patient.objects.get(pat_id=pk)
    context['email']=patient.email
    return render(request, "patient/contact_us.html", {'context': context})

def map_show(request, pk):
    context={'pk': pk, 'coords': [[19.117131, 72.90463, 'Ahuja Pranav'], [19.091104, 72.935005, 'Hardik Asher'], [19.150748, 72.903066, 'Tushar Bapecha'], [19.210506, 72.908963, 'Animesh Chaturvedi'], [19.091289, 72.957334, 'Karan Bhanushali'], [19.198571, 72.982563, 'Rugved Bongale'], [19.230356, 72.939008, 'Ronak Gala'], [19.161097, 72.960605, 'Akshat Gandhi'], [19.240368, 72.996704, 'Anchal Jain'], [19.133163, 72.978785, 'Joshi Saurav'], [19.129233, 72.932369, 'Rama Daugherty'], [19.179661, 72.93291, 'Ignatius Vincent'], [19.282513, 72.899229, 'Nasim Garrett'], [19.225142, 72.936886, 'Xander Franco'], [19.246724, 72.991944, 'Russell Ochoa'], [19.124205, 72.934343, 'Howard Fleming'], [19.097097, 72.976609, 'Beverly Hood'], [19.167572, 72.914159, 'Ahmed Sanchez'], [19.275186, 72.988254, 'Paul Mcguire'], [19.225481, 72.963841, 'Phelan Stout']]}
    return render(request, 'doctor/map_show.html', {'context': context})

def profile(request,pk):
    patient=Patient.objects.get(pat_id=pk)
    context={'pk': pk, 'patient': patient}
    if request.method == "POST":
        patient.name=request.POST.get('name')
        patient.email=request.POST.get('email')
        patient.save()
    return render(request,'patient/profile.html',{'context': context})

def feed(request, pk):
    posts=PostDb.objects.all()
    context={'pk': pk, 'posts': posts}
    print(posts[0].title)
    return render(request, 'patient/feed.html', {'context': context})
