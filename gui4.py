from tkinter import *


class App:
	def __init__(self, master):
		self.master = master
		master.title("my first gui with my first OOP")
		master.geometry("500x300")

		self.canvas = Canvas(master, width=500, height=500, bg="cyan")
		self.canvas.place(relx = 0.5, rely=0.5, anchor=CENTER)


		self.button_1 = Button(master, text="click to close", fg="black", font=("Fixedsys", 20), bg="red", command=master.quit)
		self.button_1.place(relx=1, rely=0, anchor=NE)



class App2:
	def __init__(self, main):
		self.main = main
		main.title("my second widget")
		main.geometry("1000x1000")

		self.frame = Frame(main, width=1000, height=1000, bg="orange")
		self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

		self.frame2 = Frame(main, width = 500, height = 500, bg = "cyan")
		self.frame2.place(relx=0.5, rely=0.5, anchor=N)

		def on_click():
			root2 = Tk()
			root2.geometry("1000x1000")
			root2.title("new stuff")
			frame3 = Frame(root2, width=1000, height=1000, bg="purple")
			frame3.place(relx=0.5, rely=0.5, anchor=CENTER)
			# BUTTON:
			btn = Button(root2, text="click boi", fg="green", bg="yellow", font=("Fixedsys",22), command=root.quit)
			btn.place(relx=1, rely=0, anchor=NE)

		self.button = Button(main, text="click to go to next page", fg="spring green", bg="cyan", font=("Fixedsys", 30), command=on_click)
		self.button.place(relx=1, rely=0, anchor=NE)

root = Tk()
My_gui1 = App2(root)
root.mainloop()