from django import forms
from app.models import Project,User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['uname','uphone','uemail','ugender','upwd']