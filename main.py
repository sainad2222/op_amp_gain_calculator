from tkinter import Tk, Label, Button, StringVar, DISABLED, NORMAL, Scale, Entry
from tkinter.constants import CENTER, HORIZONTAL, NSEW, S
from PIL import ImageTk, Image


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
        self.answer = '0'

        # master label
        self.label = Label(
            master, text="Operational amplifier Gain calculator")
        self.label.grid(row=0,column=0)

        # Buttons
        self.invert_button = Button(
            master, text="Inverting", command=self.switch_type)
        self.invert_button.configure(state=DISABLED)
        self.invert_button.grid(row=1,column=0)
        self.non_invert_button = Button(
            master, text="Non Inverting", command=self.switch_type)
        self.non_invert_button.configure(state=NORMAL)
        self.non_invert_button.grid(row=1,column=1)

        # images
        # create objects
        invert_image = Image.open('./inverting.png')
        self.invert_image_pi = ImageTk.PhotoImage(invert_image)
        non_invert_image = Image.open('./non_inverting.png')
        self.non_invert_image_pi = ImageTk.PhotoImage(non_invert_image)

        # show images
        self.img = Label(image=self.invert_image_pi)
        self.img.grid(row=2,column=0)

        # Gain label
        self.gain_label = Label(master, text=self.gain_label_text)
        self.gain_label.grid(row=3,column=0)

        # Inputs
        rf_label = Label(master, text='RF: ', fg='black',bg='white')
        rf_label.grid(row=4,column=0)
        self.rf_entry = Entry(master)
        self.rf_entry.grid(row=4,column=1)
        rin_label = Label(master, text='RIN: ',fg='black',bg='white')
        rin_label.grid(row=5,column=0)
        self.rin_entry = Entry(master)
        self.rin_entry.grid(row=5,column=1)

        # Calculate
        self.calculate = Button(master, text="Calculate",
                                command=self.calculate_answer)
        self.calculate.grid(row=6,column=0)

        self.final_label = Label(
            master, text=self.answer, fg='black', bg='white')
        self.final_label.grid(row=7,column=0)

        # FIN
        self.close_button = Button(master, text="Close", command=master.quit,fg='red',bg='white')
        self.close_button.grid(row=8,column=0)

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
        self.final_label.configure(text=self.answer)


root = Tk()
app = App(root)
root.geometry("600x600")
root.mainloop()
