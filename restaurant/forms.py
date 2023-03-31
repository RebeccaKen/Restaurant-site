from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3}),
        }