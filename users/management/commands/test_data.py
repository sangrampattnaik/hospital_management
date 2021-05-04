from django.core.management.base import BaseCommand
import django
from django.db import IntegrityError
from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment, Account, PatientLog

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

            self.stdout.write(self.style.SUCCESS('Test data created'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR('Inetegrety error occured...create manually'))
        except django.db.utils.OperationalError:
            self.stdout.write(self.style.ERROR('No table found...run command "make migrate" (OR) "python manage.py migrate"'))
