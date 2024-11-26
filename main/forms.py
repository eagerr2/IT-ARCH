from django import forms
from django.contrib.auth.forms import AuthenticationForm, User
from .models import Order, PaymentDetail

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'delivery_option']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['card_name', 'card_number', 'expiry_date', 'cvv']