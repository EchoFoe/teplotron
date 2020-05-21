from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = Customer
        exclude = ['created', 'updated']
