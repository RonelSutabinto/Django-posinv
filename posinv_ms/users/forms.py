from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    password1 = forms.CharField(min_length=8, max_length=30, widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        # help_texts = {
        #     'username': 'same as your roll no.',
        # }

    # def save(self, commit: True):
    #     user = super(UserForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #     return user

    def clean_password(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 4:
            raise ValidationError('Password too short')
        return super(UserCreationForm, self).clean_password1()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

