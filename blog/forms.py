from django import forms
from .models import Category,Post


class PostSearchForm(forms.Form):
    c=forms.ModelChoiceField(
         queryset=Category.objects.all().order_by('name'))
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = 'Category'
       