from django import forms
from .models import *

class mainitemform(forms.ModelForm):
    class Meta:
        model = mainitem   
        fields = "__all__"

class FirutForm(forms.ModelForm):
    class Meta:
        model = Firut
        fields = "__all__"

class VegetablesForm(forms.ModelForm):
    class Meta:
        model = Vegetables
        fields = "__all__"

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"


class requesstfomr(forms.ModelForm):
    class Meta:
        model = request
        fields = "__all__"

class sellproductform(forms.ModelForm):
    class Meta:
        model = sellproduct
        fields = "__all__"