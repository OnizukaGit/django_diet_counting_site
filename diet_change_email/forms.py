from django import forms
from django.contrib.auth.models import User


class ResetMailForm(forms.ModelForm):
    new_email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

    def clean_new_email(self):
        new_email = self.cleaned_data.get('new_email')
        if new_email == self.instance.email:
            raise forms.ValidationError("Musisz podać inny mail niż ten który chcesz zmienić")
        return new_email