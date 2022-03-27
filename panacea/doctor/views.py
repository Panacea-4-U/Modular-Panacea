from django.shortcuts import render
from panacea_app.models import Patient, TempDb, Doctor
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