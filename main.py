from tkinter import *
import pandas 
import random
words_dict={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
    #words_dict=[{"French":row.French, "English":row.English} for (index, row) in data.iterrows()]
except (FileNotFoundError,IndexError):
    data=pandas.read_csv("data/french_words.csv")
    #words_dict=[{"French":row.French, "English":row.English} for (index, row) in data.iterrows()]
    words_dict=data.to_dict(orient="records")
else:
    words_dict=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    
    current_card=random.choice(words_dict)
    #print(current_card)
    canvas.itemconfig(french_text, text="French",fill="black")
    canvas.itemconfig(french_word, text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=my_image)
    flip_timer=window.after(3000, flip_card)
def if_known():
    if current_card in words_dict:
        words_dict.remove(current_card)
    print(len(words_dict))
    data=pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
# window.minsize(width=600, height=500)
window.title("Flashy")
#window.minsize(width=600, height=500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image=PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=my_image)
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(french_text, text="English",fill="white")
    canvas.itemconfig(french_word, text=current_card["English"],fill="white")

flip_timer=window.after(3000, flip_card)
window.after_cancel(flip_card)
#jhggkkjgkjg

french_text=canvas.create_text(400, 180, text="French", font=("Ariel", 40, "bold"))
french_word=canvas.create_text(400,263,text="word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,bg=BACKGROUND_COLOR, highlightthickness=0,command=if_known)
right_button.grid(row=1, column=1)
wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)
window.mainloop()