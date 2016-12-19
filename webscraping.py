import webbrowser
from Tkinter import *

master = Tk()
e=Entry(master)
e.pack()

e.focus_set()

temp=''
def callback():
	temp=e.get()
	

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()

mainloop()

print(temp)
#urlpath = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+temp


#webbrowser.open(urlpath)

