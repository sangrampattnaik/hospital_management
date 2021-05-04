from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment
from django import forms


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class PhysicianSpecialityForm(forms.ModelForm):
    class Meta:
        model = PhysicianSpeciality
        fields = "__all__"

class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = "__all__"

class PatientTreatmentForm(forms.ModelForm):
    class Meta:
        model = PatientTreatment
        fields = "__all__"
