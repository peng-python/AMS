from django import forms


class AddUserForm(forms.Form):
    mobile = forms.CharField(required=True, max_length=11)


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=8)