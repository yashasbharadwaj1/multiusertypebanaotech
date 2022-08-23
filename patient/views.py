from django.shortcuts import render,redirect
from doctor.models import Appointment


from multiusertype.models import User
# Create your views here.

def quick_appointment(request):
	
	user_name=request.user
	appointment_list = Appointment.objects.all().order_by("-user")
	q=request.GET.get("q")#search start
	if q:
		appointment_list=appointment_list.filter(user__first_name__icontains=q)
	else:
		appointment_list = appointment_list# search end

	appointments= {
		    "query": appointment_list,
		    "user_name":user_name
	}
	return render(request, 'patient_quick_appointment.html', appointments )

def patient_appointments(request):#this section for my appointment

	user_name=request.user
		#Getting all Post and Filter By Logged UserName
	appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with=user_name)
    
	q=request.GET.get("q")#search start
	if q:
		appointment_list=appointment_list.filter(user__first_name__icontains=q)
	else:
		appointment_list = appointment_list# search end

	appointments= {
		    "query": appointment_list,
		    "user_name":user_name,    
	}
	return render(request, 'patient_appointment.html', appointments )

def appointment_book(request, id):#activate after clicking book now button
	
	user_name=request.user.get_username()
	single_appointment= Appointment.objects.get(id=id)
	form = single_appointment
	form.appointment_with=user_name
	form.save()
	return redirect('patient:patient_appointments')
	

	
	