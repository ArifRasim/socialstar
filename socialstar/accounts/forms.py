from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].label = 'Email Address'
        # self.fields['username'].widget.attrs.update({'class': 'form-control'})
        # self.fields['email'].widget.attrs.update({'class': 'form-control'})
        # self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        # self.fields['password2'].widget.attrs.update({'class': 'form-control'})
