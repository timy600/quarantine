from tkinter import messagebox, Tk, Label, Button
import webbrowser
import time
from random import randint

count_list = 0
url_list = []
url_list.append({'url': "youtube.com", 'message': "woaw, ok, why not..."})
url_list.append({'url': "lemonde.fr", 'message': "lemonde"})
url_list.append({'url': "elpais.com", 'message': "elp pais"})

url_list_random = []
url_list_random.append({'url': "wired.com", 'message': "test"})
url_list_random.append({'url': "elpais.com", 'message': "test2"})
url_list_random.append({'url': "google.com", 'message': "test3"})
# open the GUI

window = Tk()
window.wm_title("Alfred, your assistant")
messagebox.showinfo("Presentation","Hi, I'm Jarvis your personal thought processing assistant")

""" Functions"""
def open_browser():
    global count_list
    time.sleep(1)
    if count_list < len(url_list):
        messagebox.showinfo("Result",url_list[count_list]['message'])
        time.sleep(1)
        webbrowser.open_new(url_list[count_list]['url'])
        count_list = count_list + 1
    else:
        random_count = randint(0, len(url_list_random))
        messagebox.showinfo("Result",url_list_random[random_count]['message'])
        time.sleep(1)
        webbrowser.open_new(url_list_random[random_count]['url'])

"""Value Entry"""
l1 = Label(window, text ="Hi, I'm Jarvis your personal thought processing assistant", width = 100)
l1.grid(row = 0, column = 1)

l2 = Label(window, text ="Please start thinking about something and press this button", width = 100)
l2.grid(row = 1, column = 1)

"""Buttons"""
b1 = Button(window, text = "What do I want", width=12, command = open_browser)
b1.grid(row = 4, column = 1)

window.mainloop()
# transform to an exe program
