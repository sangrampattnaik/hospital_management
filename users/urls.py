from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('patient-get/', views.PatientList.as_view(),name="patient-get"),
    path('patient-create/', views.PatientCreate.as_view(),name="patient-create"),
    path('patient-update/<pk>/', views.PatientUpdate.as_view(),name="patient-update"),

    path('physician-speciality-get/', views.PhysicianSpecialityList.as_view(),name="physician-speciality-get"),
    path('physician-speciality-create/', views.PhysicianSpecialityCreate.as_view(),name="physician-speciality-create"),
    path('physician-speciality-update/<pk>/', views.PhysicianSpecialityUpdate.as_view(),name="physician-speciality-update"),



    path('event-category-get/', views.EventCategoryList.as_view(),name="event-category-get"),
    path('event-category-create/', views.EventCategoryCreate.as_view(),name="event-category-create"),
    path('event-category-update/<pk>/', views.EventCategoryUpdate.as_view(),name="event-category-update"),


    path('patient-treatment-get/', views.PatientTreatmentList.as_view(),name="patient-treatment-get"),
    path('patient-treatment-create/', views.PatientTreatmentCreate.as_view(),name="patient-treatment-create"),
    path('patient-treatment-update/<pk>/', views.PatientTreatmentUpdate.as_view(),name="patient-treatment-update"),
    path('patient-treatment-delete/<pk>/', views.PatientTreatmentDelete.as_view(),name="patient-treatment-delete"),
]
