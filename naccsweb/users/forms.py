from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")

        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username exists")

        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if confirm != password:
            raise ValidationError("Passwords do not match")
        
        return self.cleaned_data

    username = forms.CharField(label="Username", max_length=32)
    email    = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm  = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)