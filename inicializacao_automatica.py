import os
import sys
from win32com.client import Dispatch

def create_shortcut(target, shortcut_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target
    shortcut.save()

def add_to_startup():
    # Caminho para o executável
    executable_path = os.path.abspath(sys.argv[0])
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, 'main.lnk')

    create_shortcut(executable_path, shortcut_path)

    executable_path = os.path.abspath(sys.argv[0])
    startup_folder = os.path.join('C:', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, 'main.lnk')

    create_shortcut(executable_path, shortcut_path)
