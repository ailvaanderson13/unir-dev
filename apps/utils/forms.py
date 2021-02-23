from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Informe seu e-mail:'
            }
        )
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'classs': 'form-control', 'placeholder': 'Informe seua Senha:'
            }
        )
    )