import pyautogui as pg

# 화면 크기
print(pg.size())

# 마우스 위치
print(pg.position())

# 마우스 이동
pg.moveTo(400, 30)

# 마우스 클릭
pg.click()
pg.click(button='right')

pg.moveTo(1500, 450)
pg.click()
pg.doubleClick()
pg.moveTo(1500, 550)
pg.doubleClick()
pg.tripleClick()

# 마우스 드래그
# (500, 25)에서 (500, 500)까지 0.2초 동안 드래그
pg.moveTo(500, 25, 0.2)
pg.dragTo(500, 500, 0.2)

pg.moveTo(500, 200)
pg.click()

# 마우스 스크롤
pg.scroll(1000)
pg.scroll(-500)