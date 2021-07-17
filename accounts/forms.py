from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()


# Sign Up Form
class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'First Name...'}), max_length=200,
                                 required=True, )
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'Last Name...'}), max_length=200,
                                required=True, )
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Email address..."}), required=True,
                            max_length=75)
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter phone..."}), required=True,
                            max_length=75)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password..."}),
                               validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm password..."}),
                                       validators=[validate_password])

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
