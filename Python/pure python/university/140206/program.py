from tkinter import *

# gui
root = Tk()

# frame
frame = Frame(root)


# میخوام به فریم خود یک سری شکل اضافه کنم
frame.pack()

button = Button(frame, text="test")

# دکمه رو اضافه کن به صفحه ای که داریم
button.pack()


# برای اجرا شدن برنامه این خط کد را در نهایت قرار میدهیم
root.mainloop()