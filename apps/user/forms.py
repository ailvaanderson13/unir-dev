from django import forms
from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primeiro nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'insira seu nome'
            }
        )
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu sobrenome'
            }
        )
    )

    email = forms.CharField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu e-email'
            }
        )
    )

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
    first_name = forms.CharField(
        label='Primeiro nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'insira seu nome'
            }
        )
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu sobrenome'
            }
        )
    )

    email = forms.CharField(
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu e-email'
            }
        )
    )

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
        label='Redefinir Senha',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check'
            }
        )
    )

    motorista = forms.BooleanField(
        required=False,
        label='Motorista',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check'
            }
        )
    )

    passageiro = forms.BooleanField(
        required=False,
        label='Passageiro',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'celular', 'motorista', 'passageiro'
        ]