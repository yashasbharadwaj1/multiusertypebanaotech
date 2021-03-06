
from django.urls import path
from .import views

app_name='multiusertype'
urlpatterns=[
    path('',views.index,name='index'),

    path('login/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),


    path('logout', views.logout, name='logout'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
]  

