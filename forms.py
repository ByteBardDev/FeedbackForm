
from django import forms

class FeedbackForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='User Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    feedback_message = forms.CharField(widget=forms.Textarea, label='Feedback Message')

    # Custom clean method for additional validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        # Ensure passwords match
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        # Ensure phone number is at least 10 digits and contains only numbers
        if not phone_number.isdigit() or len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long and contain only numbers.")
