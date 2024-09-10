import mss
import mss.tools
import os
import subprocess
import platform
import time
from datetime import datetime

def get_image_dir():
    if platform.system() == "Windows":
        dir = "imagens"
        os.makedirs(dir, exist_ok=True)
        subprocess.run(['attrib', '+H', dir], check=True) # Pasta Oculta.
    else:
        dir = ".imagens"
        os.makedirs(dir, exist_ok=True)
    return dir

dir = get_image_dir()

with mss.mss() as sct:
    while True:
        monitors = sct.monitors
        timestamp = datetime.now().strftime("%d.%m.%Y_%H_%M_%S")
        for i,monitor in enumerate(monitors[1:], start=1):
            screenshot = sct.grab(monitor)
            nome_arquivo = os.path.join(dir, f'monitor_{i}_{timestamp}.png') #Usamos o os.path.join para salvar na nossa pasta
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=nome_arquivo)
    
        time.sleep(60)