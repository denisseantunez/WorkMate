from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from workmates.models import workmateUser
from tasks.models import Tasks, TaskProfile

class WorkmateUserCreationForm(UserCreationForm):
    class Meta:
        model = workmateUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class WorkmateTaskCreationForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'category', 'priority', 'user')

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        return task
    
class WorkmateTaskAssign(ModelForm):
    class Meta:
        model = TaskProfile
        fields = ('user', 'task')

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
        return task
