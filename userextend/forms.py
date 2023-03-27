from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Please enter your email adress'})
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Please enter your username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Confirm your password'})

    def clean(self):
        cleaned_data = self.cleaned_data
        all_users = User.objects.filter(email__exact=cleaned_data.get('email', 'username'))
        if all_users:
            msg = f'A user with this email: {cleaned_data.get("email")}, already exists!'
            msg2 = f'A user with this username: {cleaned_data.get("username")}, already exists!'
            self._errors['email'] = self.error_class([msg])
            self._errors['username'] = self.error_class([msg2])


class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Please enter your password'})
