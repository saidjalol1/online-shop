from django import forms
from .models import CustomUser
from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

class CustomUserCreationForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
