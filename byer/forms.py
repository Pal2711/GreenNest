from django import forms
from .models import *

class sginupform(forms.ModelForm):
    class Meta:
        model = usersgimup
        fields = "__all__"

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"