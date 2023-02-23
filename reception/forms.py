from django import forms
from .models import Patient
from django import forms
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'middle_name', 'gender', 'birthdate', 'address', 'phone_number', 'diagnosis']





class PatientSearchForm(forms.Form):
    """
    Поиск пациентов по имени. Мы можем использовать класс Form и определить поле query,
    которое будет строкой поискового запроса.
    """
    query = forms.CharField(label='Поиск по имени', max_length=100)
