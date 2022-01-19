from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'job_title', 'birth_date')

        widgets = {
            'email': forms.EmailField(
                attrs={
                    'placeholder': 'Email',
                }
            ),
        }
    # email = forms.CharField(
    #     label="Email",
    #     required=True,
    #     widget=,
    # )

    # first_name = forms.CharField(
    #     label="First name",
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control form-control-lg", 'placeholder': 'First name'}),
    # )

    # last_name = forms.CharField(
    #     label="Last name",
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control form-control-lg", 'placeholder': 'Last name'}),
    # )

    # job_title = forms.CharField(
    #     label="Job title",
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control form-control-lg", 'placeholder': 'Job title'}),
    # )

    # birth_date = forms.DateField(
    #     label="Birth date",
    #     required=True,
    #     widget=forms.DateInput(
    #         attrs={"class": "form-control form-control-lg"}),
    # )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", 'placeholder': 'Password'}),
    )

    repassword = forms.CharField(
        label="Repeat password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg", 'placeholder': 'Repeat assword'}),
    )

    def clean_repassword(self):
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")
        if len(password) < 5:
            self.add_error(
                "password", "Password length must be greater than 5 characters"
            )
            return

        if password != repassword:
            self.add_error(
                "repassword", "Password and repeat password are not the same"
            )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "gender")


class LoginForm(forms.Form):
    email = forms.CharField(
        label="email",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Email or password is incorrect")
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label="Current password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    new_password = forms.CharField(
        label="New password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class EmailVerificationForm(forms.Form):
    code = forms.CharField(
        label="Verification code",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    def __init__(self, pk, *args, **kwargs):
        self.id = pk
        super(EmailVerificationForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        code = self.cleaned_data.get("code")

        if len(code) != 6:
            raise forms.ValidationError(
                "Verification code length is incorrect")

        if not User.objects.code_validation(self.id, code):
            raise forms.ValidationError("Verification code is incorrect")

        return code
