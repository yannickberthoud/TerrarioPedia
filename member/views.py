from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UpdateUserForm, ProfileForm
from django.views.generic import DetailView, ListView

from django.contrib.auth.models import User
class CommunityListView(ListView):
    model = User
    template_name = 'member/community_list.html'
    context_object_name = 'objects'
    queryset = User.objects.order_by('last_name', 'first_name')

class CommunityDetailView(DetailView):
    model = User
    template_name = 'member/community_details.html'
    context_object_name = 'object'

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'member/change_password.html'
    success_message = "Votre mot de passe a été mis à jour."
    success_url = reverse_lazy('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profil a été mis à jour.')
            return redirect(to='profile')
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'member/profile.html', {'user_form': user_form, 'profile_form': profile_form})