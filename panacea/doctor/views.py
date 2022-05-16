from ast import Add
import email
from email.headerregistry import Address
from unicodedata import name
from django.shortcuts import render, redirect
from panacea_app.models import Patient, TempDb, Doctor, Reviews, Bookmark
from .models import PostDb,  AddressDb, SpecialityDb
from django.db.models import Q
from django.views.generic.list import ListView
import itertools
import random

# Create your views here.
def home(request,pk):
    doctor=Doctor.objects.all()   
    context={'pk': pk}
    return render(request,'doctor/homepage.html',{'context': context})

def about(request, pk):
    context={'pk': pk}
    return render(request,'doctor/about_us.html',{'context': context})


def services(request, pk):
    data=Doctor.objects.filter(~Q(doc_id=pk))
    context={'data': data, 'pk':pk}
    if request.method == "POST":
        return redirect('dpdetails2', pk=pk, pk2=request.POST.get('temp_doc_id'))
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
    doctor = Doctor.objects.get(doc_id=pk)
    count = PostDb.objects.filter(doc_id=doctor.doc_id).count() 
    totalPosts = PostDb.objects.filter(doc_id=doctor.doc_id)
    speciality = SpecialityDb.objects.filter(doc_id=pk)
    context={'pk': pk, 'doctor': doctor, 'count': count, "totalPosts": totalPosts, "speciality": speciality}
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
    doctorPostCount = dict(itertools.islice(doctorPostCount.items(), 5))
    context={'pk': pk, 'posts': posts, 'doctorPostCount': doctorPostCount}
    if request.method == "POST":
        return redirect('bookmark', pk=pk, pk3=request.POST.get('idpost'))
    return render(request, 'doctor/feed.html', {'context': context})

def add_address(request, pk):
    context={'pk': pk}
    if request.method == "POST":
        new_add=AddressDb()
        new_add.doc_id=pk
        new_add.address=request.POST.get('addaddr')
        new_add.pin_code=int(request.POST.get('pincode'))
        new_add.latitude="25.2352435"
        new_add.longitude="23.222432"
        new_add.day=request.POST.get('days')
        new_add.fromtime=request.POST.get('slotfrom')
        new_add.totime=request.POST.get('slotto')
        new_add.save()
    return render(request, 'doctor/add_address.html',{'context': context})

def add_speciality(request, pk):
    context={'pk': pk}
    if request.method == "POST":
        new_spe=SpecialityDb()
        new_spe.doc_id=pk
        new_spe.speciality=request.POST.get('addspe')
        new_spe.save()
    return render(request, 'doctor/add_speciality.html',{'context': context})

def remove_address(request, pk):
    context={'pk':pk}
    all_res=AddressDb.objects.filter(doc_id=pk)
    context['address']=all_res
    if request.method=="POST":
        AddressDb.objects.filter(address=request.POST.get('address')).delete()
    return render(request, 'doctor/remove_address.html',{'context':context})

def update_doc(request, pk):
    context={'pk': pk}
    doctor=Doctor.objects.get(doc_id=pk)
    context['doctor']=doctor
    if request.method == "POST":
        doctor.name=request.POST.get('name')
        doctor.email=request.POST.get('email')
        doctor.save()
    return render(request, 'doctor/update_doc.html',{'context':context})

def dpdetails2(request, pk, pk2):
    context={'pk':pk}
    doctor=Doctor.objects.get(doc_id=pk2)
    context['doctor']=doctor
    reviews=Reviews.objects.filter(doc_id=pk2)
    context['reviews']=reviews
    speciality=SpecialityDb.objects.filter(doc_id=pk2)
    context['speciality']=speciality
    addresses=AddressDb.objects.filter(doc_id=pk2)
    context['addresses']=addresses
    if request.method=="POST":
        review=Reviews()
        review.doc_id=pk2
        review.pat_id=pk
        review.rate_1=request.POST.get('rating')
        review.review=request.POST.get('comments')
        review.speciality=request.POST.get('speciality')
        review.save()
    return render(request, 'doctor/dpdetails2.html', {'context': context})

def bookmark(request, pk, pk3):
    context={'pk': pk}
    if request.method=="POST":
        bookmark=Bookmark()
        bookmark.post_id=pk3
        bookmark.user_id=pk
        bookmark.header=request.POST.get('header')
        bookmark.save()
    return render(request, 'doctor/bookmark.html', {'context': context})

def doc_bookmark(request, pk):
    context={'pk': pk}
    bookmarks = Bookmark.objects.filter(user_id=pk)
    bookmarked_posts_id = []
    for i in bookmarks:
        bookmarked_posts_id.append(i.post_id)
    postinfo = PostDb.objects.filter(id__in=bookmarked_posts_id)
    total_content = []
    for i, j in zip(bookmarks, postinfo):
        total_content.append([i, j])
    print(total_content)
    context['bookmarks'] = total_content
    # context['postinfo'] = postinfo
    return render(request, 'doctor/doc_bookmark.html', {'context': context})
