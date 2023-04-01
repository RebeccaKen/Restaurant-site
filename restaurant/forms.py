from django import forms
from django.forms import ModelForm
from .models import Feedback, Customer

# class FeedbackForm(forms.ModelForm):
#     model = Feedback
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     comments = forms.CharField(widget=forms.Textarea)
#     rating = forms.IntegerField(label='Rating (1-5)', min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comments', 'rating']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 5}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']