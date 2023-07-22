import time
import pyautogui as pg

pg.moveTo(1500, 500)
pg.click()

# msg 키보드 입력
msg = 'Hello, world!'
pg.write(msg)

# msg 지우기
pg.press('backspace', presses=len(msg), interval=0.02)

# Caps Lock 끄고 키기
time.sleep(0.1)
pg.press('capslock')
time.sleep(0.1)
pg.press('capslock')

# 붙여넣기
pg.hotkey('ctrl', 'v')

# 0.5초 간격으로 엔터 3번
pg.press('enter', presses=3, interval=0.5)

# shift 눌렀다 떼기
pg.keyDown('shiftleft')
pg.press('a')
pg.keyUp('shiftLeft')

print(pg.KEYBOARD_KEYS)