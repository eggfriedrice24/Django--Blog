from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from users.forms import UserRegisterForm
from django.views.generic import CreateView
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# def register(request) -> HttpResponse:
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'{username} Account Has Been Created!')
#             return redirect('blog-home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

class RegisterView(SuccessMessageMixin, CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = '%(username)s Your Account Has Been Created Successfully'
    # def get_success_message(self, cleaned_data):
    #     return f'{cleaned_data["username"]} Account Has Been Created!'


@login_required
def profile(request) -> HttpResponse:
    return render(request, 'users/profile.html')
