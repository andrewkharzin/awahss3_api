from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from apps.users.profile.profile import Profile

# class UserLoginForm(forms.ModelForm):

#     email = forms.EmailField(widget=forms.TextInput(
#         attrs={
#             'type':'email',
#             'class':'form-control',
#             'placeholder':('Enter your email')
#         }
#     ))
#     password = forms.CharField(max_length=16,widget=forms.PasswordInput(
#         attrs={
#             'type': 'password',
#             'class':'form-control',
#             'placeholder':'Password'
#         }
#     ))


#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password', ]
#         unlabelled_fields = ['email', 'password', ]


#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_show_labels = True
#         for field in UserLoginForm.Meta.unlabelled_fields:
#             self.fields[field].label = False


class UserLoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'type': 'email',
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Email'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Password'
        }))

    class Meta:
        model = User
        # fields = ['email', 'password', ]
        unlabelled_fields = ['email', 'password', ]

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        for field in UserLoginForm.Meta.unlabelled_fields:
            self.fields[field].label = False


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        help_text='A valid email address, please.', required=True)

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name',
                  'second_name',
                  'last_name',
                  'position',
                  'phone',
                  'shift_work',
                  'birthday',
                  'image',
                  ]
