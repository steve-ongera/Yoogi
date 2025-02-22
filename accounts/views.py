from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "accounts/signup.html"
    form_class = RegistrationForm
    success_message = "User registration was successful"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return response


class LoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_message = "User logged in successfully"


# class LogoutView(SuccessMessageMixin, auth_views.LogoutView):
#     next_page = "/"  # Redirect to homepage after logout
#     success_message = "User logged out successfully"

#     def dispatch(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super().dispatch(request, *args, **kwargs)
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "User logged out successfully")
        return redirect("website:home")  # Change this to your desired redirect URL
