import webbrowser
from Tkinter import *

master = Tk()
master.title("Search Amazon")
e=Entry(master)
e.pack()
e.focus_set()

def callback():
	global temp
	temp=e.get()
	master.quit()	

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()

mainloop()

url='https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+temp

webbrowser.open(url)

