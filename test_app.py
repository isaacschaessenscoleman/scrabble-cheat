from tkinter import *
# for a better image system, we need to pip install Pillow
from PIL import ImageTk, Image

from script import *


# creating instance in order to create GUI Tkinter app
root = Tk()
# title in top bar (where filename usually is)
root.title('Scrabble Cheater')
# size of window when GUI opens
root.geometry('1000x1000')
# adding an icon/logo for our GUI

#root.iconbitmap('/Users/isaaccoleman/Documents/LearningtoCode/guis/test-icon.ico')


#title_label = Label(root, text='Scrabble Cheat', fg='blue', bg='black',font=("Times", "40", "bold italic"))
#title_label.pack()

def clicked():
    
    text_box.delete(1.0, END)
    #input_1.get() uses the data inputted by the user into the input_1 entry widget
    list_of_letters = list(input_1.get().lower())
    list_of_words = scrabble_cheat_list(list_of_letters)
    list_of_words = [f'{tupl[0]} : {tupl[1]}' for tupl in list_of_words]
    #my_text = Text(label_frame, text='\n'.join(list_of_words)).pack()
    text_box.insert(index = END, chars = '\n'.join(list_of_words)).pack() 
    text_box.tag_config("here", background="yellow", foreground="blue")
    #pass


instruction_label = Label(root, text='Enter your letters')
instruction_label.pack(pady=50)

input_1 = Entry(root, width = 300, font=('Helvetica', '32'))
input_1.pack()

enter_button = Button(root, text='Confirm', command=clicked)
enter_button.pack()


label_frame = LabelFrame(root, text='This is Label Frame')
label_frame.pack(expand='yes', fill='both')


scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

text_box = Text(label_frame, yscrollcommand = scroll_bar.set,  font=('Helvetica', '32'))
text_box.tag_add("center", "1.0", "1.5")
text_box.pack()

text_box.insert






# Note to user: you may want to also other letters which you can attach your given letters to

# error handling for input


root.mainloop()