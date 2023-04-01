from django import forms
from django.forms import ModelForm
from .models import Feedback, Customer


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comments', 'rating']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 5}),
        }

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ['name', 'phone', 'email', 'address']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].initial = self.instance.name
            self.fields['phone'].initial = self.instance.phone
            self.fields['email'].initial = self.instance.email
            self.fields['address'].initial = self.instance.address