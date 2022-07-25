from django import forms
from .models import Category,Post


class PostSearchForm(forms.Form):
    c=forms.ModelChoiceField(
         queryset=Category.objects.all().order_by('name'))
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = 'Category'



class DateTimeForm(forms.Form):
    date_time_field = forms.DateTimeField(label='Date Time Field',
                                          label_suffix=" : ", required=True, disabled=False,
                                          input_formats=['%Y-%m-%d %H:%M:%S'],
                                          widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
                                          error_messages={'required': "This field is required."})
   
       