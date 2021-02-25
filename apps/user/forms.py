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

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'celular'
        ]


class UserAdminForm(forms.ModelForm):
    celular = forms.CharField(
        required=False,
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Informe seu celular'
            }
        )
    )

    reset_password = forms.BooleanField(
        required=False,
        label='RESETAR SENHA',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    motorista = forms.BooleanField(
        required=False,
        label='MOTORISTA',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    passageiro = forms.BooleanField(
        required=False,
        label='PASSAGEIRO',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'celular', 'motorista', 'passageiro'
        ]