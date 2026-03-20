import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caosrj.settings')
django.setup()

from django.contrib.auth.models import User

# Configurações do seu novo Admin
username = 'ADMINISTRADORCAOS' # Pode mudar se quiser
email = 'admin@caosrj.com'
password = 'SuaSenhaAqui123' # COLOQUE UMA SENHA FORTE AQUI

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario {username} criado com sucesso!")
else:
    print(f"Superusuario {username} ja existe.")