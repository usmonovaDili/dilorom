from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistratoinForm(forms.ModelForm):
    password = forms.CharField(label='parol', widget=forms.PasswordInput)
    password2 = forms.CharField(label='parolni takrorlang', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    # foydalanuvchi kiritgan kodni tekshirish

    def clean_passwors2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('parol xato')
        return data['password2']
