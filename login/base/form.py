from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from workmates.models import workmateUser

class WorkmateUserCreationForm(UserCreationForm):
    class Meta:
        model = workmateUser
        fields = ('username', 'email', 'password1', 'password2', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
