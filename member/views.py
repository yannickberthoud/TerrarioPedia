from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UpdateUserForm

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'member/change_password.html'
    success_message = "Votre mot de passe a été mis à jour."
    success_url = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Votre profil a été mis à jour.')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'member/profile.html', {'user_form': user_form})