from django import forms

from .models import Solar_energy

class PostEnergy(forms.ModelForm):

    class Meta:
        model = Solar_energy
        fields = ('produced', 'consumed')


