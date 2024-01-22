# RPA = Robotic Process Automation (Automação Robótica de Processos)
import pyautogui as pag
import pandas as pd
import time

pag.PAUSE = 1.5

pag.press("win")
pag.write("chrome")
pag.press("enter")

time.sleep(2)

pag.click(x=247, y=644)
pag.hotkey("win", "up")
pag.write("https://lucas-dos-santos-gomes.github.io/sistema-python-power-up/")
pag.press("enter")

time.sleep(3)

pag.press("tab")
pag.write("pythonimpressionador@gmail.com")
pag.press("tab")
pag.write("python2024")
pag.press("enter")

time.sleep(2)
pag.PAUSE = 0.15

table = pd.read_csv("products.csv")
for line in table.index:
  pag.click(x=549, y=262, clicks=2)
  for column in table.columns:
    cell = table.loc[line, column]
    if not pd.isna(cell):
      pag.write(str(cell))
    pag.press("tab")
  pag.press("enter")
  pag.scroll(1000)