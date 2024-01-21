# RPA = Robotic Process Automation (Automação Robótica de Processos)
import pyautogui as pag
import time

pag.PAUSE = 1.5

pag.press("win")
pag.write("chrome")
pag.press("enter")

time.sleep(2)

pag.click(x=247, y=644)
pag.hotkey("win", "up")
pag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pag.press("enter")

pag.press("tab")
pag.write("pythonimpressionador@gmail.com")
pag.press("tab")
pag.write("python2024")
pag.press("enter")