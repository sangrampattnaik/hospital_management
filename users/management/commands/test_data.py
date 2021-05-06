from django.core.management.base import BaseCommand
import django
from django.db import IntegrityError
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment,PatientLog
import datetime

class Command(BaseCommand):
    help = "Create Test Data"

    def handle(self, *args, **kwargs):
        try:
            patient1 = Patient.objects.create(patient_id="1",patient_name="Ram")
            patient2 = Patient.objects.create(patient_id="2",patient_name="Laxman")
            patient3 = Patient.objects.create(patient_id="3",patient_name="Hanuman")
            patient4 = Patient.objects.create(patient_id="4",patient_name="Ravan")
            patient5 = Patient.objects.create(patient_id="5",patient_name="Bharat")
            patient6 = Patient.objects.create(patient_id="6",patient_name="Bheem")

            event1 = EventCategory.objects.create(event_name="Chemotherapy",category='1')
            event2 = EventCategory.objects.create(event_name="Radiation",category='1')
            event3 = EventCategory.objects.create(event_name="Immunosupressants",category='2')
            event4 = EventCategory.objects.create(event_name="BTKI",category='2')
            event5 = EventCategory.objects.create(event_name="Biopsy",category='3')

            physician1 = PhysicianSpeciality.objects.create(speciality_name="Radiologist")
            physician2 = PhysicianSpeciality.objects.create(speciality_name="Onchologist")
            physician3 = PhysicianSpeciality.objects.create(speciality_name="HematoLogist")
            physician4 = PhysicianSpeciality.objects.create(speciality_name="Onchologist")
            physician5 = PhysicianSpeciality.objects.create(speciality_name="Pathologist")
            physician6 = PhysicianSpeciality.objects.create(speciality_name="Onchologist")
            PatientTreatment.objects.bulk_create([
                PatientTreatment(patient_id=patient1,event_name=event2,physician_id=physician1),
                PatientTreatment(patient_id=patient2,event_name=event1,physician_id=physician2),
                PatientTreatment(patient_id=patient1,event_name=event5,physician_id=physician1),
                PatientTreatment(patient_id=patient3,event_name=event3,physician_id=physician2),
                PatientTreatment(patient_id=patient4,event_name=event4,physician_id=physician3),
                PatientTreatment(patient_id=patient5,event_name=event2,physician_id=physician4),
                PatientTreatment(patient_id=patient4,event_name=event1,physician_id=physician2),
                PatientTreatment(patient_id=patient1,event_name=event5,physician_id=physician5),
                PatientTreatment(patient_id=patient6,event_name=event1,physician_id=physician6),
            ])
            
            d1  = 1,datetime.date(2020,1,2),100
            d2  = 1,datetime.date(2020,1,27),200
            d3  = 2,datetime.date(2020,1,1),300
            d4  = 2,datetime.date(2020,1,21),400
            d5  = 2,datetime.date(2020,1,21),300
            d6  = 2,datetime.date(2020,1,1),500
            d7  = 3,datetime.date(2020,1,20),400
            d8  = 1,datetime.date(2020,3,4),500
            PatientLog.objects.bulk_create([
                PatientLog(account_id=d1[0],date=d1[1],patient_id=d1[2]),
                PatientLog(account_id=d2[0],date=d2[1],patient_id=d2[2]),
                PatientLog(account_id=d3[0],date=d3[1],patient_id=d3[2]),
                PatientLog(account_id=d4[0],date=d4[1],patient_id=d4[2]),
                PatientLog(account_id=d5[0],date=d5[1],patient_id=d5[2]),
                PatientLog(account_id=d6[0],date=d6[1],patient_id=d6[2]),
                PatientLog(account_id=d7[0],date=d7[1],patient_id=d7[2]),
                PatientLog(account_id=d8[0],date=d8[1],patient_id=d8[2])
            ]
            )

            self.stdout.write(self.style.SUCCESS('Test data created'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR('Inetegrety error occured...create manually'))
        except django.db.utils.OperationalError:
            self.stdout.write(self.style.ERROR('No table found...run command "make migrate" (OR) "python manage.py migrate"'))
