from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','name','password1','password2')
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['email']  # or name, depending on logic
            # Any custom logic like assigning name
            if commit:
                user.save()
            return user

