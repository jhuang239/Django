from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('name', 'email')  # Specify the fields you want to include in the form