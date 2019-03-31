from htmldom import htmldom
from pynput.keyboard import Key, Controller
import time
import pyautogui

keyboard = Controller()

dom = htmldom.HtmlDom().createDom("""

""")
elem = dom.find( "span" )
time.sleep(3)
for txt in elem:
    t = txt.text()
    keyboard.type(t)
    time.sleep(0.00001)
    pyautogui.press('space')
    
