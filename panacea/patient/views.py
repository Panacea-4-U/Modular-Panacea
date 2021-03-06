from django.shortcuts import render, redirect
from panacea_app.models import Patient, TempDb, Doctor, Reviews, Bookmark
from doctor.models import PostDb, SpecialityDb, AddressDb
from django.contrib import messages
import random
import pandas as pd
import pickle

import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'model_pkl')
file_path2 = os.path.join(module_dir, 'kidney_model_pkl')

# Create your views here.

temp_doc_id=None

def home(request, pk):
    context={'pk': pk}
    return render(request, 'patient/homepage.html', {'context': context})

def about(request, pk):
    context={'pk': pk}
    return render(request, 'patient/about_us.html', {'context': context})

def services(request, pk):
    data=Doctor.objects.all()
    context={'data': data, 'pk':pk}
    if request.method == "POST":
        return redirect('dpdetails', pk=pk, pk2=request.POST.get('temp_doc_id'))
    return render(request, 'patient/services.html',{'context': context})

def health(request, pk):
    if request.method == "POST":
        ip_info=[[request.POST.get('gender'),request.POST.get('smoker'),request.POST.get('tobacco'),request.POST.get('bp'),request.POST.get('obese'),request.POST.get('diabetes'),request.POST.get('metabolic'),request.POST.get('stimulant'),request.POST.get('cardiac'),request.POST.get('preclam'),request.POST.get('cabg'),request.POST.get('respi')]]
        ip_df=pd.DataFrame(ip_info,columns=['Gender','Chain_smoker','Consumes_other_tobacco_products','HighBP','Obese','Diabetes','Metabolic_syndrome','Use_of_stimulant_drugs','Family_history','History_of_preeclampsia','CABG_history','Respiratory_illness'])
        with open(file_path , 'rb') as f:
            dt = pickle.load(f)
        print(dt.predict(ip_df))
        if dt.predict(ip_df)==['1']:
            # data=SpecialityDb.objects.filter(speciality__iregex=r'Heart.+')
            # tempdata=[]
            # datatemp=Doctor.objects.all()
            # for i in data:
            #     for j in datatemp:
            #         if i.doc_id == j.doc_id and j not in tempdata:
            #             tempdata.append(j)
            # context={'data': tempdata, 'pk':pk, 'disease': 'heart'}
            messages.success(request, 'You are at risk')
        else:
            messages.success(request, 'You are not at risk')
    context={'pk': pk}
    return render(request, 'patient/patientdetails.html', {'context': context})

def kidney(request, pk):
    if request.method == "POST":
        ip_info=[[request.POST.get('blood_pressure'),request.POST.get('specific_gravity'),request.POST.get('serum_creatinine'),request.POST.get('sodium'),request.POST.get('haemoglobin'),request.POST.get('packed_cell_volume'),request.POST.get('peda_edema')]]
        ip_df=pd.DataFrame(ip_info,columns=['blood_pressure', 'specific_gravity', 'serum_creatinine', 'sodium', 'haemoglobin','packed_cell_volume', 'peda_edema'])
        with open(file_path2 , 'rb') as f:
            dt = pickle.load(f)
        print(dt.predict(ip_df))
        if dt.predict(ip_df)==['1']:
            messages.success(request, 'You are at risk')
        else:
            messages.success(request, 'You are not at risk')
    context={'pk': pk}
    return render(request, 'patient/kidney.html', {'context': context})

def lungs(request, pk):
    context={'pk': pk}
    return render(request, 'patient/lungs.html', {'context': context})

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
    reviews=Reviews.objects.filter(pat_id=pk)
    reviews2=[]
    for i in reviews:
        temp={}
        temp['doc_id']=i.doc_id
        temp['rate_1']=i.rate_1
        temp['review']=i.review
        doc=Doctor.objects.get(doc_id=i.doc_id)
        temp['name']=doc.name
        reviews2.append(temp)
    context['reviews']=reviews2
    if request.method == "POST":
        patient.name=request.POST.get('name')
        patient.email=request.POST.get('email')
        patient.save()
    return render(request,'patient/profile.html',{'context': context})

def pfeed(request, pk):
    posts=PostDb.objects.all().order_by('-post_date', 'doc_name')
    doctorPostCount = dict()
    doctor = Doctor.objects.all()
    for i in doctor:
        docs=PostDb.objects.filter(doc_id=i.doc_id).count()
        doctorPostCount[i.name] = docs
    doctorPostCount = dict(sorted(doctorPostCount.items(), key=lambda item: item[1], reverse=True))
    context={'pk': pk, 'posts': posts, 'doctorPostCount': doctorPostCount}
    if request.method == "POST":
        return redirect('pbookmark', pk=pk, pk3=request.POST.get('idpost'))
    return render(request, 'patient/feed.html', {'context': context})

def dpdetails(request, pk, pk2):
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
    return render(request, 'patient/dpdetails.html', {'context': context})

def pbookmark(request, pk, pk3):
    context={'pk': pk}
    if request.method=="POST":
        bookmark=Bookmark()
        bookmark.post_id=pk3
        bookmark.user_id=pk
        bookmark.header=request.POST.get('header')
        bookmark.save()
    return render(request, 'patient/bookmark.html', {'context': context})

def pat_bookmark(request, pk):
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
    return render(request, 'patient/doc_bookmark.html', {'context': context})

