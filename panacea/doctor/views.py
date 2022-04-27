import email
from unicodedata import name
from django.shortcuts import render
from panacea_app.models import Patient, TempDb, Doctor
from .models import PostDb
from django.db.models import Q
from django.views.generic.list import ListView

# Create your views here.
def home(request,pk):
    context={'pk': pk}
    return render(request,'doctor/homepage.html',{'context': context})

def about(request, pk):
    context={'pk': pk}
    return render(request,'doctor/about_us.html',{'context': context})


def services(request, pk):
    data=Doctor.objects.all()
    context={'data': data, 'pk':pk}
    return render(request, 'doctor/services.html',{'context': context})


class SearchView(ListView):
    model = Doctor
    template_name = 'doctor/services.html'
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
        return {'result': result, 'pk': self.kwargs['pk']}
    
def contact_us(request,pk):
    context={'pk': pk}
    doctor=Doctor.objects.get(doc_id=pk)
    context['email']=doctor.email
    return render(request, "doctor/contact_us.html", {'context': context})

def health(request, pk):
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
    return render(request, 'doctor/patientdetails.html', {'context': context})

def map_show(request, pk):
    context={'pk': pk, 'coords': [[19.117131, 72.90463, 'Ahuja Pranav'], [19.091104, 72.935005, 'Hardik Asher'], [19.150748, 72.903066, 'Tushar Bapecha'], [19.210506, 72.908963, 'Animesh Chaturvedi'], [19.091289, 72.957334, 'Karan Bhanushali'], [19.198571, 72.982563, 'Rugved Bongale'], [19.230356, 72.939008, 'Ronak Gala'], [19.161097, 72.960605, 'Akshat Gandhi'], [19.240368, 72.996704, 'Anchal Jain'], [19.133163, 72.978785, 'Joshi Saurav'], [19.129233, 72.932369, 'Rama Daugherty'], [19.179661, 72.93291, 'Ignatius Vincent'], [19.282513, 72.899229, 'Nasim Garrett'], [19.225142, 72.936886, 'Xander Franco'], [19.246724, 72.991944, 'Russell Ochoa'], [19.124205, 72.934343, 'Howard Fleming'], [19.097097, 72.976609, 'Beverly Hood'], [19.167572, 72.914159, 'Ahmed Sanchez'], [19.275186, 72.988254, 'Paul Mcguire'], [19.225481, 72.963841, 'Phelan Stout']]}
    return render(request, 'doctor/map_show.html', {'context': context})

def profile(request,pk):
    doctor=Doctor.objects.get(doc_id=pk)
    count = PostDb.objects.filter(doc_id=doctor.doc_id).count() 
        
    context={'pk': pk, 'doctor': doctor, 'count': count}
    if request.method == "POST":
        doctor.name=request.POST.get('name')
        doctor.email=request.POST.get('email')
        doctor.save()
    return render(request,'doctor/profile.html',{'context': context})

def make_post(request, pk):
    context={'pk': pk}
    if request.method == "POST":
        post = PostDb()
        post.doc_id=pk
        post.doc_name=Doctor.objects.get(doc_id=pk).name
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.image = request.FILES['image']
        post.save()
    return render(request, 'doctor/make_post.html', {'context': context})

def feed(request, pk):
    posts=PostDb.objects.all().order_by('-post_date', 'doc_name')
    doctorPostCount = dict()
    doctor = Doctor.objects.all()
    for i in doctor:
        docs=PostDb.objects.filter(doc_id=i.doc_id).count()
        doctorPostCount[i.name] = docs
    doctorPostCount = dict(sorted(doctorPostCount.items(), key=lambda item: item[1], reverse=True))
    context={'pk': pk, 'posts': posts, 'doctorPostCount': doctorPostCount}
    # print(posts[0].title)
    return render(request, 'doctor/feed.html', {'context': context})