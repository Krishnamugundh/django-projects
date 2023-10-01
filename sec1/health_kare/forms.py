from django import forms
from .models import pat_desc,user_input

class pat_form(forms.ModelForm):
    # pat_id = forms.IntegerField()
    # pat_name = forms.CharField(max_length=35)
    # desc = forms.TextField(max_length=100,blank=True,default='Please enter some text')
    # age = forms.PositiveIntegerField()

    class Meta:
         model = pat_desc
         fields = '__all__'
         
class new_data(forms.ModelForm):
    class Meta:
        model = user_input
        fields = '__all__'