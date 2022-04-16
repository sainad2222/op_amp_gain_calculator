from tkinter import Tk, Label, Button,StringVar,DISABLED,NORMAL,Scale, Entry
from tkinter.constants import HORIZONTAL, S
from PIL import ImageTk,Image

class App:
    def __init__(self, master):
        self.master = master
        master.title("Opamp Gain Calculator")

        # string vars
        self.cur_button = StringVar()
        self.cur_button = '1'

        self.gain_label_text = StringVar()
        self.gain_label_text = 'Gain = Rf/Rin'

        self.answer = StringVar()

        # master label
        self.label = Label(master, text="Operational amplifier Gain calculator")
        self.label.pack()

        # Buttons
        self.invert_button = Button(master, text="Inverting", command=self.switch_type)
        self.invert_button.configure(state=DISABLED)
        self.invert_button.pack()
        self.non_invert_button = Button(master, text="Non Inverting", command=self.switch_type)
        self.non_invert_button.configure(state=NORMAL)
        self.non_invert_button.pack()

        # images
        ## create objects
        invert_image = Image.open('./inverting.png')
        self.invert_image_pi = ImageTk.PhotoImage(invert_image)
        non_invert_image = Image.open('./non_inverting.png')
        self.non_invert_image_pi = ImageTk.PhotoImage(non_invert_image)

        ## show images
        self.img = Label(image=self.invert_image_pi)
        self.img.pack()

        # Gain label
        self.gain_label = Label(master,text=self.gain_label_text)
        self.gain_label.pack()

        # Inputs
        rf_label = Label(master,text='RF: ')
        self.rf_entry = Entry(master)
        self.rf_entry.pack()
        rin_label = Label(master,text='RIN: ')
        self.rin_entry = Entry(master)
        self.rin_entry.pack()

        # Calculate
        self.calculate = Button(master,text="Calculate",command=self.calculate_answer)
        self.calculate.pack()
        
        self.final_label = Label(master,textvariable=self.answer,fg='green',bg='black')
        self.final_label.pack()

        # FIN
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def switch_type(self):
        if self.cur_button == '1':
            self.invert_button.configure(state=NORMAL)
            self.non_invert_button.configure(state=DISABLED)
            self.img.configure(image=self.non_invert_image_pi)
            self.gain_label.configure(text="Gain = 1 + Rf/Rin")
            self.cur_button = '0'
        else:
            self.invert_button.configure(state=DISABLED)
            self.non_invert_button.configure(state=NORMAL)
            self.img.configure(image=self.invert_image_pi)
            self.gain_label.configure(text="Gain = Rf/Rin")
            self.cur_button = '1'

    def calculate_answer(self):
        rf_val = int(self.rf_entry.get())
        rin_val = int(self.rin_entry.get())
        if self.cur_button == '1':
            self.answer = rf_val/rin_val
        else:
            self.answer = 1 + rf_val/rin_val
        print(self.answer)
 

root = Tk()
app = App(root)
#  root.geometry("1200x700")
root.mainloop()
