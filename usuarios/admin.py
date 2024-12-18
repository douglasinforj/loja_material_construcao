from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django    #precisa ser diferenciado do admin do django
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):    #classe que da o formato do admin como vemos
    form = UserChangeForm                        #informamos o form criado sobrescrito
    add_form = UserCreationForm                  #informamos o form criado sobrescrito
    model = Users                                #infomramos o forme que será utilizado(personalizado)
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields':('cargo',)}),
    )
    