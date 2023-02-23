from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Patient, Doctor
from .forms import PatientForm


class PatientListView(View):
    """Представление списка пациентов"""

    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'patient_list.html', {'patients': patients})


class PatientDetailView(View):
    """Представление детальной информации о пациенте"""

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patient_detail.html', {'patient': patient})


class PatientCreateView(View):
    """Представление создания нового пациента"""

    def get(self, request):
        form = PatientForm()
        return render(request, 'patient_form.html', {'form': form})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = Doctor.objects.get(pk=request.POST.get('doctor'))
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
        return render(request, 'patient_form.html', {'form': form})


class PatientUpdateView(View):
    """Представление редактирования информации о пациенте"""

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(instance=patient)
        return render(request, 'patient_form.html', {'form': form})

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = Doctor.objects.get(pk=request.POST.get('doctor'))
            patient.save()
            return redirect('patient_detail', pk=patient.pk)
        return render(request, 'patient_form.html', {'form': form})


class PatientDeleteView(View):
    """Представление удаления пациента"""

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patient_confirm_delete.html', {'patient': patient})

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return redirect('patient_list')
