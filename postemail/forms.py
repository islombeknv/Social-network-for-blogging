from django import forms

from postemail.models import EmailModel


class EmailModelForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        exclude = ['created_at']