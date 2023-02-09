from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )

        username = forms.CharField(widget=forms.TextInput())
        password = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        data = self.cleaned_data

        if data.get('password') == data.get('password2'):
            return data['password2']
        raise forms.ValidationError('Error in passwords')