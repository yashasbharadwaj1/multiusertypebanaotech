from django.urls import path
from .import views

app_name='patient'
from .views import(
	patient_appointments,
	quick_appointment,
	appointment_book,
	)

urlpatterns = [
    path('patient_appointment/', views.patient_appointments, name='patient_appointments'),
    path('quick_appointment/', views.quick_appointment, name='quick_appointment'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),
      
]
