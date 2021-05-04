from django.shortcuts import render
import pdb
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment
from django.urls import reverse_lazy
from . import forms
from django.views import generic

def index(request):
    patient_treatments = PatientTreatment.objects.filter(event_name__category="1")
    procedure_physicians = []
    unique_physician = []
    count = 0
    count_physician = {}
    for patient in patient_treatments:
        procedures = {}
        procedures[patient.physician_id.speciality_name] = patient.physician_id.id
        procedure_physicians.append(procedures)
    for physician in procedure_physicians:
        if physician not in unique_physician:
            unique_physician.append(physician)
    for _ in unique_physician:
        for key,value in _.items():
            if key not in count_physician:
                count_physician[key] = 1
            else:
                count_physician[key] += 1
    return render(request,"index.html",{"count_physician":count_physician})


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

