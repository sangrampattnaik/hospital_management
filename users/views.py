from django.shortcuts import render
import pdb
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment,PatientLog
from django.urls import reverse_lazy
from . import forms
from django.views import generic
from .utils import calculate_unique_patient,count_unique_physician

def index(request):
    count_physician = count_unique_physician(PatientTreatment)
    count_unique_patient = calculate_unique_patient(PatientLog)
    return render(request,"index.html",{"count_physician":count_physician,"count_unique_patient":count_unique_patient})


class PatientList(generic.ListView):
    model = Patient

class PatientCreate(generic.CreateView):
    model = Patient
    fields = "__all__"

class PatientUpdate(generic.UpdateView):
    model = Patient
    fields = ['patient_name']






class PhysicianSpecialityList(generic.ListView):
    model = PhysicianSpeciality


class PhysicianSpecialityCreate(generic.CreateView):
    model = PhysicianSpeciality
    fields = "__all__"

class PhysicianSpecialityUpdate(generic.UpdateView):
    model = PhysicianSpeciality
    fields = ['speciality_name']




class EventCategoryList(generic.ListView):
    model = EventCategory

class EventCategoryCreate(generic.CreateView):
    model = EventCategory
    fields = "__all__"

class EventCategoryUpdate(generic.UpdateView):
    model = EventCategory
    fields = ['event_name','category']



class PatientTreatmentList(generic.ListView):
    model = PatientTreatment

class PatientTreatmentCreate(generic.CreateView):
    model = PatientTreatment
    fields = "__all__"

class PatientTreatmentUpdate(generic.UpdateView):
    model = PatientTreatment
    fields = ['patient_id','event_name','physician_id']

class PatientTreatmentDelete(generic.DeleteView):
    model = PatientTreatment
    success_url = reverse_lazy("patient-treatment-get")


class PatientLogList(generic.ListView):
    model = PatientLog

class PatientLogCreate(generic.CreateView):
    model = PatientLog
    fields = "__all__"

class PatientLogUpdate(generic.UpdateView):
    model = PatientLog
    fields = ['account_id','date','patient_id']

class PatientLogDelete(generic.DeleteView):
    model = PatientLog
    success_url = reverse_lazy("patient-log-get")

