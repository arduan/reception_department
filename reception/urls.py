from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list_view, name='patient_list'),
    path('new/', views.patient_create_view, name='patient_new'),
    path('<int:pk>/edit/', views.patient_update_view, name='patient_edit'),
    path('<int:pk>/delete/', views.patient_delete_view, name='patient_delete'),
    path('search/', views.patient_search_view, name='patient_search'),
]
