from redditor import Reddit
reddit = Reddit()


from tkinter import *

root = Tk()
root.title("Reddit finder")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w - 100 # смещение от середины
h = h - 100
root.geometry('400x200+{}+{}'.format(w, h))

with open('./keys', 'r') as file:
    content = file.readlines()
    keys = [i.split('\n')[0] for i in content]
    file.close()

key_in_list = iter(keys)

def click_next():
    global label_text
    label_text = next(key_in_list)
    Label(text=label_text, width=20, height=3).place(relx=0.3, rely=0.2)
    reddit.next_tab()


Button(text="Next", width=20, command=click_next).place(relx=0.3, rely=0.6)
root.mainloop()