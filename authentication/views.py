from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .forms import SignupForm
from django.views.generic import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


class SignupView(View):
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return self.render_to_response(
            {'form': form, 'page_title': 'Cadastro'})

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)

            messages.success(self.request, 'Usuario cadastrado com sucesso.')
            return redirect('finance:home')

        return self.render_to_response(
            {'form': form, 'page_title': 'cadastro'}
        )

    def render_to_response(self, context):
        return render(self.request, self.template_name, context)


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f'Usuário {self.request.user} logado com sucesso.')
        return response


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('authentication:login'))
