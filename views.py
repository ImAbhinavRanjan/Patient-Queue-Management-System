from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from landing.models import Patients,Doctors
# Create your views here.

def main(request):
    return render(request,"landing/main.html")

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login")) 
    return render(request, "logged")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('logged'), {'user': request.user})
        else:
            return render(request,"landing/userlogin2.html")
    return render(request,"landing/userlogin.html")


def logged(request):
    # Get the current logged-in user
    current_user = request.user

    # Retrieve the patient instance associated with the current user
    try:
        instance = Patients.objects.get(name=current_user)
        bool_s = instance.appointment
    except Patients.DoesNotExist:
        # Handle the case when the patient instance does not exist
        bool_s = None

    # Initialize variables
    app = None
    doc_name = None
    cur_app = None
    

    if bool_s: 
        try:
           
            doctor_id = instance.doctor_id_id  # Retrieve doctor_id
            doctor_instance = Doctors.objects.get(doctor_id=doctor_id)  # Fetch Doctors instance using doctor_id
            
            app = instance.app_number
            doc_name = doctor_instance.Doc_name
            cur_app = doctor_instance.Current_appointment
            
        
        except Doctors.DoesNotExist:
            # Handle the case when the Doctors instance does not exist
            pass

    context = {
        'bool_s': bool_s,
        'app': app,
        'doc_name': doc_name,
        'cur_app': cur_app,
        
    }
    
    # Render the template with the context
    return render(request, "landing/logged.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def book(request):
    x1=1
    y1=2
    x=Doctors.objects.get(pk=x1)
    y=Doctors.objects.get(pk=y1)

    x_curr=x.Current_appointment
    x_tot=x.Total_appointment
    y_curr=y.Current_appointment
    y_tot=y.Total_appointment

    context = {
        'x_curr':x_curr,
        'y_curr':y_curr,
        'x_tot':x_tot,
        'y_tot':y_tot,
    }

    return render(request,"landing/book.html",context)

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctors, pk=doctor_id)    
    doctor.Total_appointment += 1
    doctor.save()

    current_user = request.user
    instance = get_object_or_404(Patients, name=current_user)
    instance.appointment = True
    instance.doctor_id=doctor
    instance.app_number=doctor.Total_appointment

    instance.save()

    return HttpResponseRedirect(reverse("logged"))

def doc1(request):
    patients=Patients.objects.all().filter(doctor_id=1,appointment=True).order_by('app_number')

    instance = Doctors.objects.get(doctor_id=1)
    
    curr=instance.Current_appointment
    tot=instance.Total_appointment
    context={
        'tot':tot,
        'curr':curr,
        'patients':patients
    }       

    return render(request,'landing/doc1.html',context)

def doc1inc(request, doctor_id):
    doctor = get_object_or_404(Doctors, pk=1)
    temp= doctor.Current_appointment
    doctor.Current_appointment += 1
    doctor.save()

   
    if doctor.Current_appointment != 1:
        instance=Patients.objects.get(app_number=temp,doctor_id=1)
        instance.appointment=False
        instance.app_number=0
        instance.save()

    return HttpResponseRedirect(reverse("doc1"))

def doc1Reset(request):
    doctor = get_object_or_404(Doctors, pk=1)
    doctor.Current_appointment=0
    doctor.Total_appointment=0
    doctor.save()
    return HttpResponseRedirect(reverse("doc1"))


def doc2(request):
    patients=Patients.objects.all().filter(doctor_id=2,appointment=True).order_by('app_number')

    instance = Doctors.objects.get(doctor_id=2)
    
    curr=instance.Current_appointment
    tot=instance.Total_appointment
    context={
        'tot':tot,
        'curr':curr,
        'patients':patients
    }       

    return render(request,'landing/doc2.html',context)

def doc2inc(request, doctor_id):
    doctor = get_object_or_404(Doctors, pk=2)
    temp= doctor.Current_appointment
    doctor.Current_appointment += 1
    doctor.save()

   
    if doctor.Current_appointment != 1:
        instance=Patients.objects.get(app_number=temp,doctor_id=2)
        instance.appointment=False
        instance.app_number=0
        instance.save()

    return HttpResponseRedirect(reverse("doc2"))


def doc2Reset(request):
    doctor = get_object_or_404(Doctors, pk=2)
    doctor.Current_appointment=0
    doctor.Total_appointment=0
    doctor.save()
    return HttpResponseRedirect(reverse("doc2"))