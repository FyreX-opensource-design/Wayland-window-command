from config2.config import config
from util import GetWindow
import os

configList = config.get()
currentWindow = None
savedWindow = None

while True:
    currentWindow = GetWindow.getActiveWindowLinuxWayland()
    for key, value in configList.items():
        if currentWindow == key and currentWindow != savedWindow:
            os.system(value)
            savedWindow = currentWindow