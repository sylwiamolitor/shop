from django import forms
from django.core.exceptions import ValidationError


TEXT_WIDGET = forms.TextInput(attrs={"class": "form-control"})
PASSWORD_WIDGET = forms.PasswordInput(attrs={"class": "form-control"})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    password = forms.CharField(max_length=100, widget=PASSWORD_WIDGET)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    password = forms.CharField(max_length=100, widget=PASSWORD_WIDGET)
    confirm_password = forms.CharField(max_length=100, widget=PASSWORD_WIDGET)

    first_name = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    last_name = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    email = forms.EmailField(widget=TEXT_WIDGET)

    address_1 = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    address_2 = forms.CharField(max_length=100, widget=TEXT_WIDGET, required=False)
    town_city = forms.CharField(max_length=100, label="Town/city", widget=TEXT_WIDGET)
    postcode = forms.CharField(max_length=12, widget=TEXT_WIDGET)
    country = forms.CharField(max_length=100, widget=TEXT_WIDGET)

    def clean_confirm_pw(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Passwords don\'t match!',
                code='password_mismatch'
            )
        return password2


class EditUserForm(forms.Form):
    password = forms.CharField(max_length=100, widget=PASSWORD_WIDGET, required=False)
    confirm_password = forms.CharField(max_length=100, widget=PASSWORD_WIDGET, required=False)

    first_name = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    last_name = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    email = forms.EmailField(widget=TEXT_WIDGET)

    address_1 = forms.CharField(max_length=100, widget=TEXT_WIDGET)
    address_2 = forms.CharField(max_length=100, widget=TEXT_WIDGET, required=False)
    town_city = forms.CharField(max_length=100, label="Town/city", widget=TEXT_WIDGET)
    postcode = forms.CharField(max_length=12, widget=TEXT_WIDGET)
    country = forms.CharField(max_length=100, widget=TEXT_WIDGET)

    def clean_confirm_pw(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Passwords don\'t match!',
                code='password_mismatch'
            )
        return password2
