from django.dispatch import receiver     #vai observar se teve mudandaça de estado de uma determinada classe
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role   #quem vai definir pelo comportamento quem tera as permissoes

@receiver(post_save, sender=Users)                           #Após salva e escutando nossa classe User ele fara essas ações
def define_permissoes(sender, instance, created, **kwargs):
    #caso eu esteja criando um usuário como vendedor "V"
    if created:
        if instance.cargo == "V":
            assign_role(instance, 'vendedor')      #Será atribuido a ele grupo de permissões "vendedor" automaticamente as permissões criadas em role.py
        elif instance.cargo == "G":
            assign_role(instance, 'gerente')