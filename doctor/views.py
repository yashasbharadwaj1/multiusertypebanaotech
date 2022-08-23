from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib import messages
from .forms import AppointmentForm
# Create your views here.


def doctorappointmentview(request):  # this section for my appointment

    user_name = request.user  # Getting Username

    # Getting all Post and Filter By Logged UserName
    appointment_list = Appointment.objects.all().order_by(
        "-id").filter(user=request.user)
    q = request.GET.get("q")  # search start
    if q:
        appointment_list = appointment_list.filter(
            appointment_with__icontains=q)
    else:
        appointment_list = appointment_list  # search end

    appointments = {
        "query": appointment_list,
        "user_name": user_name
    }
    return render(request, 'doctorappointment.html', appointments)


def doctor_appointment_list(request):

    user_name = request.user  # Getting Username

    # Getting all Post and Filter By Logged UserName
    appointment_list = Appointment.objects.all().order_by(
        "-id").filter(user=request.user)
    q = request.GET.get("q")  # search start
    if q:
        appointment_list = appointment_list.filter(date__icontains=q)
    else:
        appointment_list = appointment_list  # search end

    appointments = {
        "query": appointment_list,
        "user_name": user_name,
        "form": AppointmentForm(),
    }
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        saving = form.save(commit=False)
        saving.user = request.user
        saving.save()
        messages.success(request, 'Post Created Sucessfully')
    return render(request, 'create_appointment.html', appointments)


def appointment_delete(request, id):
    single_appointment = Appointment.objects.get(id=id)
    single_appointment.delete()
    messages.success(request, 'Your appointment was updated.')
    return redirect('http://127.0.0.1:8000/doctor/create_appointment/')


def appointment_update(request, id):

    user_name = request.user  # Getting Username

    # Getting all Post and Filter By Logged UserName
    appointment_list = Appointment.objects.all().order_by(
        "-id").filter(user=request.user)
    q = request.GET.get("q")  # search start
    if q:
        appointment_list = appointment_list.filter(date__icontains=q)
    else:
        appointment_list = appointment_list  # search end

    single_appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST or None, instance=single_appointment)
    if form.is_valid():
        saving = form.save(commit=False)
        saving.user = request.user
        saving.save()
        messages.success(request, 'Post Created Sucessfully')
        return redirect('http://127.0.0.1:8000/doctor/create_appointment/')

    appointments = {
        "query": appointment_list,
        "user_name": user_name,
        "form": form,
    }

    return render(request, 'appointment_update.html', appointments)
