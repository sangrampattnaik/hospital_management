from django.shortcuts import render
import pdb
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment, Account, PatientLog

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

