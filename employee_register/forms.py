from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ValidationError

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Repeat Login Password:',
                                       widget=forms.PasswordInput(attrs={'class': 'password required w-100'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email','image','password','confirm_password')

# def clean_first_name(self):
#     first_name =self.cleaned_data.get('first_name')
#     if not  first_name.isalpha():
#         raise ValidationError("First name is not valid!")
#     else:
#         return first_name