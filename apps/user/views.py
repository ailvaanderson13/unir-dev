from django.shortcuts import render
from . import forms, models


def new_user(request, pk=None):
    page_title = "NOVO USUÁRIO" if not pk else "EDITAR USUÁRIO"
    form = forms.UserForm() if not request.user.is_superuser else forms.UserAdminForm()

    if pk:
        usuario = models.User.objects.get(pk=pk)
        if usuario:
            form = forms.UserForm(instance=usuario) if not request.user.is_superuser else \
                forms.UserAdminForm(instance=usuario)

    if request.method == 'POST':
        if usuario:
            form = forms.UserForm(request.POST, instance=usuario) if not request.user.is_superuser else \
                forms.UserAdminForm(request.POST, instance=usuario)
        else:
            form = forms.UserForm(request.POST) if not request.user.is_superuser else \
                forms.UserAdminForm(request.POST)
        try:
            if form.is_valid():
                if usuario:
                    form.save()
                else:
                    new_user = form.save(commit=False)
                    new_user.username = new_user.email
                    password = new_user.celular
                    new_user.set_password(password)
                    new_user.save()
                # new_user.user = new_user.email
        except Exception as error:
            print(error)

    context = {
        'page_title': page_title, 'form': form
    }

    return render(request, 'cadastro_usuario.html', context)


def list_user(request):
    page_title = 'USUÁRIOS CADASTRADOS'

    users = models.User.objects.filter(is_active=True)

    context = {
        'users': users, 'page_title': page_title
    }

    return render(request, 'usuarios_cadastrados.html', context)

