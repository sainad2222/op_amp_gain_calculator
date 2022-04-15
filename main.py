from tkinter import Tk, Label, Button,StringVar,DISABLED,NORMAL
from PIL import ImageTk,Image

class App:
    def __init__(self, master):
        self.master = master
        master.title("Opamp Gain Calculator")

        # string vars
        self.cur_button = StringVar()
        self.cur_button = '1'

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


        # FIN
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def switch_type(self):
        if self.cur_button == '1':
            self.invert_button.configure(state=NORMAL)
            self.non_invert_button.configure(state=DISABLED)
            self.img.configure(image=self.non_invert_image_pi)
            self.cur_button = '0'
        else:
            self.invert_button.configure(state=DISABLED)
            self.non_invert_button.configure(state=NORMAL)
            self.img.configure(image=self.invert_image_pi)
            self.cur_button = '1'
 

root = Tk()
app = App(root)
root.geometry("1200x700")
root.mainloop()
