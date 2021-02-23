from django.shortcuts import render
from django.contrib.auth import authenticate, login
from apps.utils.forms import LoginForm


def page_inital(request):
    return render(request, 'page_initial/home.html')


def acessar(request):
    erro = False
    mensagem = None

    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
        else:
            erro =True
            mensagem = 'Verifique usuário e senha digitados e tente novamente'

    formulario = LoginForm()
    context = {
        'form': formulario, 'erro': erro, 'mensagem': mensagem
    }
    return render(request, 'login/login.html', context)
