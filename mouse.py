import os
from pynput.mouse import Listener
import platform

def get_mouse_file():
    if platform.system() == "Windows":
        arq2 = "mouse.txt"

        if not os.path.exists(arq2):
            open(arq2, "w")
            os.system(f"attrib +h {arq2}")
        else:
            os.remove(arq2) #Para resetar as informações toda vez que o computador for ligado e desligado
            open(arq2, "w")
            os.system(f"attrib +h {arq2}")
    else:
        arq2 = ".mouse.txt"
        if not os.path.exists(arq2):
            open(arq2, "w").close()
        else:
            os.remove(arq2) #Para resetar as informações toda vez que o computador for ligado e desligado
            open(arq2, "w").close()
    return arq2

arq2 = get_mouse_file()

"""def movimentacao(x,y):
    print(f"Mouse se moveu para ({x},{y})")"""
# Caso queira pegar movimentação em tempo "real"

def click(x, y, button, pressed):
    try:
        with open(arq2, "a") as arquivo:
            arquivo.write(f"Botão {button} {'pressionado' if pressed else 'liberado'} na posição {x} {y}\n")
    except Exception as e:
        arquivo.write(f"Erro ao gravar clique do mouse: {e}")

"""def rolagem(x, y, dx, dy):
    print(f"Rolagem na posição ({x}, {y}) com dx={dx} e dy={dy}")"""
# Caso queira captar a rolagem do mouse

with Listener(on_click=click) as listener:
    listener.join()