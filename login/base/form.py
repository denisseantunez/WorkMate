from django.forms import ModelForm, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from workmates.models import workmateUser
from tasks.models import Tasks, TaskProfile

class WorkmateUserCreationForm(UserCreationForm):
    class Meta:
        model = workmateUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DateInput(DateTimeInput):
    input_type = 'date'

class WorkmateTaskCreationForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'datelimit', 'category', 'priority', 'user', 'progress')
        widgets = {
            'datelimit': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
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
