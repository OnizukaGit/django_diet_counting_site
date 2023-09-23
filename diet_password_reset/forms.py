from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user rounded'}),
        label="Nowe Hasło"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user rounded'}),
        label="Powtórz hasło"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('old_password')
