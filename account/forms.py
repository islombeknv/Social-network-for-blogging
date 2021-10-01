from django import forms

from account.models import ProfileModel


class AccountModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user', 'created_at']