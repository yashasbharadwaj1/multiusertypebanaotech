from django.urls import path
from .import views

app_name='doctor'
urlpatterns = [
    
    path('my_appointment/', views.doctorappointmentview, name='doctor_appointment'),
    path('create_appointment/', views.doctor_appointment_list, name='doctor_appointment_list'),
    path('create_appointment/delete/<int:id>/', views.appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', views.appointment_update,name='appointment_update'),  
    
]
