from tkinter import messagebox, Tk, Label, Button
import webbrowser
import time
from random import randint

count_list = 0
url_list = []
url_list.append({'url': "wired.com", 'message': "Oh, Wired, sure, that could be interesting"})
url_list.append({'url': "elpais.com", 'message': "Ha, you want to practice your spanish, ok"})
url_list.append({'url': "https://fivethirtyeight.com/politics/", 'message': "Oh, the latest updated on the american campaign? Sure, let's ask Nate Silver"})

url_list_random = []
url_list_random.append({'url': "wired.com", 'message': "Oh, Wired, sure, that could be interesting"})
url_list_random.append({'url': "elpais.com", 'message': "Ha, you want to practice your spanish, ok"})
url_list_random.append({'url': "https://fivethirtyeight.com/politics/", 'message': "Oh, the latest updated on the american campaign? Sure, let's ask Nate Silver"})
url_list_random.append({'url': "https://www.reddit.com/r/StarWarsLeaks/", 'message': "hum, ok, more Star Wars"})
url_list_random.append({'url': "http://chevee-en-quarantaine.ga/", 'message': "I don't think Chevee worked on it recently"})
url_list_random.append({'url': "lemonde.fr", 'message': "Here it is, the latest about the Coronavirus"})
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
