from tkinter import messagebox, Tk, Label, Button
import webbrowser
import time
count_list = 0
url_list = []
url_list.append({'url': "youtube.com", 'message': "woaw, ok, why not..."})
url_list.append({'url': "lemonde.fr", 'message': "lemonde"})
url_list.append({'url': "elpais.com", 'message': "elp pais"})


# open the GUI

window = Tk()
window.wm_title("Alfred, your assistant")
messagebox.showinfo("Presentation","Hi, I'm Jarvis your personal thought processing assistant")
    #dict('url': "wired.com", 'message': "wired"),
    #dict('url': "fivethirtyeight.com", 'message': "sure, go get some news about the Coronavirus"),
    #dict('url': "https://www.netflix.com/fr-en/title/81115994", 'message': "Tiger King?! I knooow it's incredible isn't it?!"),

"""
url_list_random = [
    dict('url': "youtube.com", 'message': "woaw, ok, why not..."),
    dict('url': "lemonde.fr", 'message': "lemonde"),
    dict('url': "elpais.com", 'message': "elp pais"),
    dict('url': "wired.com", 'message': "wired"),
    dict('url': "fivethirtyeight.com", 'message': "sure, go get some news about the Coronavirus"),
    dict('url': "https://www.netflix.com/fr-en/title/81115994", 'message': "Tiger King?! I knooow it's incredible isn't it?!"),
]
"""
""" Functions"""
def open_browser():
    global count_list
    time.sleep(1)
    if count_list < len(url_list):
        messagebox.showinfo("Result",url_list[count_list]['message'])
        time.sleep(1)
        webbrowser.open_new(url_list[count_list]['url'])

    """
    else:
        random_count = randint(0, len(url_list_random))
        messagebox.showinfo("Result",url_list[count_list]['message'])
        time.sleep(1)
        webbrowser.open_new(url_list[count_list]['url'])
    """
    count_list = count_list + 1
    print(count_list)

    #url = "https://youtube.com"
    #webbrowser.open_new(url)

"""Value Entry"""
l1 = Label(window, text ="Hi, I'm Jarvis your personal thought processing assistant", width = 100)
l1.grid(row = 0, column = 1)

l2 = Label(window, text ="Please start thinking about something and press this button", width = 100)
l2.grid(row = 1, column = 1)
"""
link_text = StringVar()
e1 = Entry(window, width = 45, textvariable = link_text)
e1.grid(row = 0, column = 2, columnspan = 3)

t1 = Text(window, height = 1, width = 34)
t1.grid(row = 1, column = 2, columnspan = 3)
"""
"""Buttons"""
b1 = Button(window, text = "What do I want", width=12, command = open_browser)
b1.grid(row = 4, column = 1)

window.mainloop()

# prompt for name

# first response
# wait 3 seconds
# open the browser

# hazard responses from list with message + URL

# transform to an exe program
