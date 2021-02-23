from django import forms
from .models import User

class UserForm(forms.ModelForm):
    celular = forms.CharField(
        required=True,
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Informe seu celular'
            }
        )
    )

    reset_password = forms.BooleanField(
        required=True,
        label='RESETAR SENHA',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    model = User
    fields = [
        'first_name', 'last_name', 'email', 'celular'
    ]