from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'current-password', 'placeholder':'Old Password', 'autofocus': True,}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'new-password', 'placeholder':'New Password',}),
        strip=False,
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'new-password', 'placeholder':'Confirm New Password',}),
    )