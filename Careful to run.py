from tkinter import *
from tkinter import messagebox

def fix():
	while True:
		if(messagebox.askyesno(title="Fixing problem!", message="There is a humble virus!\nDo you wanna delete it?")):
			while True:
				if(messagebox.askyesno(title="Hackerman needs permission",icon="error", message="Hello Sir! Nice to meet you.\nFor bad programming I'm so\nweak. So Please sir,I want\nyou to give me permission\nto delete one of your\nimportant files.\nThanks in advance.")):
					pass
				else:
					while True:
						if(messagebox.askyesno(title="Are you comedy me?",icon="warning", message="Hello Sir!\nHackerman is not to weak,\nand thus you cannot ignore me.")):
							break


w = Tk()

messagebox.showwarning(title="warning",
		message="Something is wrong!\nYou should fix it now!!!")
w.config(background="black")
T = Label(w,
	fg="red",
	bg="black",
	font=("Ariel",7),
	text="I found a problem in your system!\nClick here to fix your problem.\n(Superuser permission isn't needed!)")
T.pack()

f = Button(w,
	text="Fix It Now!",
	bg="silver",
	fg="red",
	font=("Ariel",13,"bold"),
	command=fix)
f.pack()

w.mainloop()