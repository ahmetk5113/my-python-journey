from tkinter import *

main = Tk()
main.geometry("1000x1000")
main.title("Welcome")
canvas = Canvas(main, width = 1500, height = 1000, bg = "spring green")
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)


frame = Frame(main)
frame = Frame(main, width = 500, height = 500, bg = "cyan")
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

frame3 = Frame(main, width=300, height=300, bg="orange")
frame3.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# LABEL:
lbl = Label(main, text = "Hi", fg = "deep pink", font = ("Fixedsys",30), bg = "spring green")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# FUNCTION FOR BUTTON:

def on_click():
	root = Tk()
	frame2 = Frame(root)
	frame2 = Frame(root, width = 1000, height = 1000, bg = "cyan")
	frame2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
	root.geometry("700x700")
	root.title("SUP")
	label_new = Label(root, text = "There you go :)", font = ("Fixedsys", 22), fg = "red", bg = "black")
	label_new.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# BUTTON:

btn = Button(main, text = "this is a button", fg = "blue", font = ("Fixedsys",20), bg = "dark turquoise", command=on_click)
btn.place(relx = 1.0, rely = 0.0, anchor = NE)

main.mainloop()
