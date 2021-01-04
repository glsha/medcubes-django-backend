from django import forms
from .models import Form

class MedcubesForm(forms.ModelForm):
    
    class Meta: 
        model = Form
        fields = ('name','email','subject','contact','body')