import pyautogui as pg

buttonLoc = pg.locateOnScreen('sample/five.png')
print(buttonLoc)

pg.moveTo(buttonLoc)
pg.tripleClick()

center = pg.center(buttonLoc)
print(center)
