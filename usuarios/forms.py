from django import forms 
from django.contrib.auth import forms
from .models import Users

#sobrescrevendo os forms para usar o nosso personalizado
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users                       #indicaremos qual o model utilizar

#sobrescrevendo os forms para usar o nosso personalizado
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users                       #indicaremos qual o model utilizar