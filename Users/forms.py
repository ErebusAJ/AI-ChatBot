from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class self:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
