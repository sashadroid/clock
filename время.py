from tkinter import *
import time

root = Tk()

clock = Label(root, font=('Trebuchet MS', 20, 'bold'), bg='Black', fg='White')
clock.pack(fill=BOTH, expand=1)

sign = Label(root, font=('Trebuchet MS', 7, 'bold'), bg='Black', fg='White',
             text='---------🔪---------время лечит---------🔪---------')
sign.pack(side=BOTTOM)


def tick():
    time1 = time.strftime('%H:%M:%S')
    clock.config(text='☠ '+time1+' ☠')
    clock.after(200, tick)


tick()
root.geometry('205x55')
root.title('время')
root['bg'] = 'Black'
root.mainloop()
