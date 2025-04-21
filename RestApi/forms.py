from .models import City
from django import forms


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'location': forms.TextInput(),  # désactive la carte
        }

class RoadForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'geometry': forms.TextInput(),  # désactive la carte
        }