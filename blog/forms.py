from django import forms
from .models import Category, Post


class PostSearchForm(forms.Form):
    c = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = 'Category'


class BookingForm(forms.Form):

    required_speciality = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    doctor_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    patient_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    date_of_appointment = forms.DateTimeField(
        label='Date of appointment',
        label_suffix=" / ",
        required=True,
        disabled=False,
        input_formats=['%m/%d/%Y'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
        error_messages={'required': "This field is required."})
    starttimeofappointment = forms.TimeField(label='start time ')
