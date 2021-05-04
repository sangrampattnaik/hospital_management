from users.models import Patient,PhysicianSpeciality, EventCategory, PatientTreatment, Account, PatientLog
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

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class PatientLogForm(forms.ModelForm):
    class Meta:
        model = PatientLog
        fields = "__all__"
