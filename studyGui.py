from tkinter import *
from tkinter import ttk
import glob
from PIL import Image, ImageTk
from random import randint

#from yapsy.PluginManager import PluginManager
TIME = [
    5,
    10,
    15,
    20
]
IMAGES = [
    'Colours',
    'Basic shapes',
    'Images'
]
class StudyGui(object):
    def __init__(self):
        # Create window instance

        self.win = Tk()
        self.win.title('EEG Study')
        self.image_dir = glob.glob('/Images/Images/')
        self.shapes_dir = glob.glob('/Images/Basic shapes/')
        self.colours_dir = glob.glob('./Images/Colours/*.jpg')
        self.counter = 0
        # Create the containers to hold widgets

        #Startbutton container
        self.buttonFrame = ttk.Frame(self.win)
        self.buttonFrame.grid(column=2, row=2, padx=20, pady=5, sticky='S')
        # Plugin selection
        #
        self.labelsFrame1 = LabelFrame(self.win, background='white', text='Settings:')
        self.labelsFrame1.grid(column=0, row=0, padx=20, pady=5, sticky='N')
        # Port selection
        #
        self.labelsFrame2 = ttk.LabelFrame(self.win, text='')
        self.labelsFrame2.grid(column=0, row=1, padx=20, pady=5, sticky="WE")

        # Board type selection
        #
        self.labelsFrame3 = ttk.LabelFrame(self.win, text='')
        self.labelsFrame3.grid(column=1, row=0, padx=20, pady=5, sticky='N')
        # ==========================
        # Adding menus
        # ==========================

        # Creating a Menu Bar
        #
        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)

        # Add menu items
        # Placeholder code so I can see how to write menus
        self.fileMenu = Menu(self.menuBar, tearoff=0)

        self.fileMenu.add_command(label="Reset", command=self.reset)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        # Add an actions menu
        # Placeholder code so I can see how to write menus
        self.actionMenu = Menu(self.menuBar, tearoff=1)
        self.actionMenu.add_command(label="Initialise board", command=self.connect_board, accelerator="Cmd+I")
        self.menuBar.add_cascade(label="Actions", menu=self.actionMenu)

        # =====================
        # Adding settings menu
        # =====================

        #Dropdown menu for image selection
        self.image_var = StringVar(self.win)
        self.image_var.set(IMAGES[0]) #Default value
        self.sel_images = OptionMenu(self.labelsFrame1, self.image_var, *IMAGES).grid(row=0,column=1, sticky=W)
        self.label_sel_img = Label(self.labelsFrame1, text="Select Images:").grid(column=0, row=0, sticky=W)

        #Dropdown menu for time selection
        self.time_var = IntVar(self.win)
        self.time_var.set(TIME[1]) #Defaul value
        self.sel_time = OptionMenu(self.labelsFrame1, self.time_var, *TIME).grid(row=1, column=1, sticky=W)
        self.label_sel_time = Label(self.labelsFrame1, text = "Select Time:", justify=LEFT).grid(row=1, column=0, sticky=W)

        #Radio buttons for order
        self.order_var = IntVar()
        self.sel_order1 = Radiobutton(self.labelsFrame1, text = "Set", variable = self.order_var, value = 0).grid(row=2, column=1, sticky=W)
        self.sel_order2 = Radiobutton(self.labelsFrame1, text = "Random", variable = self.order_var, value = 1).grid(row=3, column=1, sticky=W)
        self.label_sel_order = Label(self.labelsFrame1, text="Select order:").grid(row=2, column=0, sticky=W)

        #Add startbutton
        self.start_button = Button(self.buttonFrame, text='Start Study', padx=10, command=self.studyStart).grid(row=0, column=1)

        #Add quit study button
        self.quit_button = Button(self.buttonFrame, text='Quit Study', padx=10, command=lambda: self.study_screen.destroy()).grid(row=0, column=0)

    def start(self):
        self.win.mainloop()

    def reset(self):
        self.win.quit()

    def connect_board(self):
        pass

    # ====================================
    # Create a fullscreen Toplevel window
    # ====================================

    def studyStart(self):

        def removeInstr(event=None):
            self.study_instructions.pack_forget()

        def showImage(counter, event=None):
            print(counter)
            if self.order_var.get() == 0:
                if counter < len(self.image_list):
                    self.im = self.image_list[counter]
                    self.image_label.configure(image=self.im)
                    counter += 1
                    self.study_screen.after(self.time_var.get()*1000, showImage, counter)
                else:
                    pass

        def openImages(self):
            img_list = []
            for i in range(len(self.colours_dir)):
                x = ImageTk.PhotoImage(Image.open(self.colours_dir[i]))
                img_list.append(x)
                print('tjo')
            return img_list

        self.study_screen=Toplevel(bg='black')

        # Make sure the the window is in fullscreen mode.
        self.w, self.h = self.study_screen.winfo_screenwidth(), self.study_screen.winfo_screenheight()
        self.study_screen.overrideredirect(1)
        self.study_screen.geometry("%dx%d+0+0" % (self.w, self.h))


        # Make the new window focused.
        self.study_screen.focus_set()  # <-- move focus to this widget
        self.instr_txt='Welcome to my EEG study.\n\r You will be shown several screens of stimuli with ' \
                            ' a black screen in between.\n\r Please simply focus on the screen.\n\r\n\r ' \
                            'Press Enter to start the study.'

        #Write the study instructions
        self.study_instructions = Label(self.study_screen, text=self.instr_txt)
        self.study_instructions.config(fg='white', bg='black', pady=500, font=('Palatino', 28))
        self.study_instructions.pack()
        self.image_label = Label(self.study_screen)
        self.image_label.pack()
        self.image_list = openImages(self)
        # Remove the Label when any key is pressed
        self.study_screen.bind('<Return>',removeInstr, showImage(self.counter))
        #self.study_screen.bind('<F1>', showImage(self.counter))
        self.study_screen.bind("<Escape>", lambda e: e.widget.quit())

eeg = StudyGui()

eeg.start()