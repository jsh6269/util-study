import pyautogui as pg

pg.alert(text='message box', title='title', button='OK')
pg.confirm(text='confirm box', title='title', buttons=['OK', 'Cancel'])

msg = pg.prompt(text='prompt box', title='title', default="write here")
print(msg)

psw = pg.password(text='password box', title='title', mask='*')
print(psw)