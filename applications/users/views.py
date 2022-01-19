from django.views.generic import View, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .forms import (
    UserRegisterForm,
    LoginForm,
    UpdatePasswordForm,
    EmailVerificationForm,
)
from .models import User
from .functions import code_generator


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_app:panel")

    def form_valid(self, form):
        register_code = code_generator()
        user = User.objects.create_user(
            form.cleaned_data["email"],
            form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            gender=form.cleaned_data["gender"],
            register_code=register_code,
        )

        subject = "Confirmation email"
        message = f"Verification code: {register_code}"
        sender = "eliashhtorres@gmail.com"
        send_mail(subject, message, sender, [form.cleaned_data["email"]])

        return redirect(reverse("users_app:verify", kwargs={"pk": user.id}))


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("users_app:panel")

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class PanelView(LoginRequiredMixin, ListView):
    template_name = "users/panel.html"
    context_object_name = "user_favorites"
    login_url = reverse_lazy("users_app:login")

    def get_queryset(self):
        return User.objects.get_user_favorites(self.request.user)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("users_app:login"))


class UpdatePasswordView(LoginRequiredMixin, FormView):
    login_url = "users_app:login"
    template_name = "users/update_password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy("users_app:login")

    def form_valid(self, form):
        user = self.request.user
        auth = authenticate(
            username=user.username,
            password=form.cleaned_data["password"],
        )
        if auth:
            user.set_password(form.cleaned_data["new_password"])
            user.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = "users/code_verification.html"
    form_class = EmailVerificationForm
    success_url = reverse_lazy("users_app:login")

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({"pk": self.kwargs["pk"]})
        return kwargs

    def form_valid(self, form):
        User.objects.filter(id=self.kwargs["pk"]).update(is_active=True)
        return super(CodeVerificationView, self).form_valid(form)
