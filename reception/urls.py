from django.urls import path
from .views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/new/', PatientCreateView.as_view(), name='patient_new'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
