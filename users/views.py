from django.shortcuts import render
import pdb
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment, Account, PatientLog

def index(request):
    patient_treatments = PatientTreatment.objects.filter(event_name__category="1")
    procedure_physicians = []
    unique_physician = []
    count = 0
    for patient in patient_treatments:
        d = {}
        d[patient.physician_id.speciality_name] = patient.physician_id.physician_id
        procedure_physicians.append(d)
    for physician in procedure_physicians:
        if physician not in unique_physician:
            unique_physician.append(physician)
    for i in unique_physician:
        print(i)
            
        
    return render(request,"index.html")