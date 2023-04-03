from django import forms
from django.forms import ModelForm
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comments', 'rating']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 5}),
        }


