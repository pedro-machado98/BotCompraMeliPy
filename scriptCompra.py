import pyautogui
import time




# 1330 460

# (left=881, top=318, width=91, height=77)
# (x=926, y=356)

try:
    flag = pyautogui.locateCenterOnScreen('cupomNegado.png')
    print(flag.x)
    x = flag.x
    y = flag.y
    while (flag != None):
        pyautogui.click(x=x, y=y)
        time.sleep(0.50)
        flag = pyautogui.locateCenterOnScreen('cupomNegado.png')
finally:
    time.sleep(1)
    pyautogui.click(x=1330, y=460)
    time.sleep(2)
    compra = pyautogui.locateCenterOnScreen('confirmarCompra.png')
    xCompra = compra.x
    yCompra = compra.y
    pyautogui.click(x=xCompra, y=yCompra)

