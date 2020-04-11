from tkinter import *
import webbrowser

# open the GUI

window = Tk()
window.wm_title("Alfred, your assistant")
messagebox.showinfo("Presentation","Hi, I'm Jarvis your personal thought processing assistant")
"""Value Entry"""
l1 = Label(window, text ="Hi, I'm Jarvis your personal thought processing assistant", width = 30)
l1.grid(row = 0, column = 1)

l2 = Label(window, text ="Please start thinking about something and press this button", width = 16)
l2.grid(row = 1, column = 1)

link_text = StringVar()
e1 = Entry(window, width = 45, textvariable = link_text)
e1.grid(row = 0, column = 2, columnspan = 3)

t1 = Text(window, height = 1, width = 34)
t1.grid(row = 1, column = 2, columnspan = 3)

"""Buttons"""
b1 = Button(window, text = "Ajouter", width=12, command = add_command)
b1.grid(row = 4, column = 1)

window.mainloop()

# prompt for name

# first response
# wait 3 seconds
# open the browser

# hazard responses from list with message + URL

# transform to an exe program
url = "https.//youtube.com"
webbrowser.open_new(url)
