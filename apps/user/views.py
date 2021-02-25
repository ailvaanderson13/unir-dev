from django.shortcuts import render
from . import forms


def new_user(request):
    page_title = "NOVO USUÁRIO"
    form = forms.UserForm() if not request.user.is_superuser else forms.UserAdminForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST) if not request.user.is_superuser else forms.UserAdminForm(request.POST)
        try:
            if form.is_valid():
                form.save()
        except Exception as error:
            print(error)

    context = {
        'page_title': page_title, 'form': form
    }

    return render(request, 'cadastro_usuario.html', context)