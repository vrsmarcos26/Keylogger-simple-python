import os
from pynput.mouse import Listener

arq2 = "mouse.txt"
open(arq2, "w")
os.system(f"attrib +h {arq2}")

"""def movimentacao(x,y):
    print(f"Mouse se moveu para ({x},{y})")"""
# Caso queira pegar movimentação em tempo "real"

def click(x, y, button, pressed):
    with open(arq2, "a") as arquivo:
        arquivo.write(f"Botão {button} {'pressionado' if pressed else 'liberado'} na posição {x} {y}\n")

"""def rolagem(x, y, dx, dy):
    print(f"Rolagem na posição ({x}, {y}) com dx={dx} e dy={dy}")"""
# Caso queira captar a rolagem do mouse

with Listener(on_click=click) as listener:
    listener.join()