from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=3,unique=True)
    patient_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.patient_id}"

    class Meta:
        ordering = ['patient_id']


class PhysicianSpeciality(models.Model):
    speciality_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}"

    def save(self,*args,**kwargs):
        self.speciality_name = self.speciality_name.capitalize()
        super(PhysicianSpeciality,self).save(*args,**kwargs)

class EventCategory(models.Model):
    category_choice = [('1','Procedure'),('2','Prescription'),('3','Test')]

    event_name = models.CharField(max_length=50)
    category = models.CharField(max_length=5,choices=category_choice,default='1')

    def __str__(self):
        return f"{self.event_name}"

class PatientTreatment(models.Model):
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    event_name = models.ForeignKey(EventCategory,on_delete=models.CASCADE)
    physician_id = models.ForeignKey(PhysicianSpeciality,on_delete=models.CASCADE)


class Account(models.Model):
    account_id = models.CharField(max_length=3,unique=True)

class PatientLog(models.Model):
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    date = models.DateField()
