#!/usr/bin/env python
# coding: UTF-8
#Program är ett hänga gubbe-spel skrivet av Anton, Antonina, Fanny och Tom.
from Tkinter import *
from random import randint
import tkMessageBox
class GUI(Frame):
    """Klass som skapar GUI och sköter alla funktioner i programmet."""
    def __init__(self,master):
        """Skapar huvudfönster och definierar klassens attribut"""
        self.lst = []
        self.btndct = {}
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.fetch()
        self.buttonize()
        self.textboxes()
        self.mainframe
        self.photo1 = PhotoImage(file='1.gif')
        self.photo2 = PhotoImage(file='2.gif')
        self.photo3 = PhotoImage(file='3.gif')
        self.photo4 = PhotoImage(file='4.gif')
        self.photo5 = PhotoImage(file='5.gif')
        self.photo6 = PhotoImage(file='6.gif')
        self.photo7 = PhotoImage(file='7.gif')
        self.photo8 = PhotoImage(file='8.gif')
        self.photo9 = PhotoImage(file='9.gif')
        self.photo10 = PhotoImage(file='10.gif')
        self.counter = 1
        self.hang1 = Canvas(self.mainframe,width=400, height=400)
        self.hang1.pack()        
        self.HangTheMan()
        self.pack(fill=BOTH,expand=1)
        self.life = 9
        self.kvar = len(self.word)        
        master.minsize(width=1024,height=768)
         
    def buttonize(self):
        """Skapar och placerar knapparna som representerar bokstäver och att starta ett nytt spel."""
        bottomframe=Frame(self)
        bottomframe.pack(fill=BOTH,side = BOTTOM)
        insideframe=Frame(bottomframe)
        insideframe.pack(pady=10)
        buttonframe=Frame(bottomframe)
        buttonframe.pack(side=BOTTOM)
        self.pack(fill=BOTH,side=BOTTOM)
        for bok in u'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.bokbtn = Button(insideframe, text = bok, command=lambda bokstav=bok:self.writer(bokstav))
            self.bokbtn.pack(side='left')
            self.btndct[bok]=self.bokbtn
        self.bttn2 = Button(buttonframe,text = 'New Game',command=lambda: self.reset(root)).pack(padx=10)
            
    def writer(self,bok):
        """Tar knappens bokstav som argument och kontrollerar den mot bokstäverna i ordet.
        Ifall rätt bokstav gissas på ändras färgen på bokstaven så den blir synlig för spelaren.
        Kallar på funktioner för att ändra spelets tillstånd.
        """
        miss=True
        for label in self.lst:
            if bok == label.cget('text'):
                label.config(fg='black')
                self.kvarmod(1)
                miss=False
        if miss:
            self.counter = self.counter+1
            self.lifemod(1)
        self.btndct[bok].config(state=DISABLED)
        self.HangTheMan()
        self.update()
   
    def textboxes(self):
        """Skapar rätt antal rutor med bokstäverna ur ordet.
        Bokstäverna är vita för att inte visas till spelaren. Lägger till bokstäverna till en lista"""
        self.mainframe = Frame(self,relief=GROOVE,borderwidth=2)
        self.mainframe.pack(fill=BOTH,expand=1)
        textboxframe = Frame(self.mainframe)
        textboxframe.pack()
        for letter in self.word:
            v = StringVar()
            letterframe = Label(textboxframe, textvariable=v, relief=GROOVE,borderwidth=3,bg="white",fg='white',width=10,height=5)
            v.set(letter)
            self.lst.append(letterframe)
            letterframe.pack(side = LEFT, padx=10,pady=100)
            
    def HangTheMan(self):
        """Visar bilderna på gubben som blir hängd beroende på spelets tillstånd."""
        self.photo1 = PhotoImage(file='1.gif')
        self.photo2 = PhotoImage(file='2.gif')
        self.photo3 = PhotoImage(file='3.gif')
        self.photo4 = PhotoImage(file='4.gif')
        self.photo5 = PhotoImage(file='5.gif')
        self.photo6 = PhotoImage(file='6.gif')
        self.photo7 = PhotoImage(file='7.gif')
        self.photo8 = PhotoImage(file='8.gif')
        self.photo9 = PhotoImage(file='9.gif')
        self.photo10 = PhotoImage(file='10.gif')       
        if self.counter == 1:
            self.hang1.create_image(200,200,image=self.photo1)
        elif self.counter==2:
            self.hang1.create_image(200,200,image=self.photo2)
        elif self.counter ==3:
            self.hang1.create_image(200,200,image=self.photo3)
        elif self.counter ==4:
            self.hang1.create_image(200,200,image=self.photo4)            
        elif self.counter ==5:
            self.hang1.create_image(200,200,image=self.photo5)
        elif self.counter ==6:
            self.hang1.create_image(200,200,image=self.photo6)
        elif self.counter ==7:
            self.hang1.create_image(200,200,image=self.photo7) 
        elif self.counter ==8:
            self.hang1.create_image(200,200,image=self.photo8)
        elif self.counter ==9:
            self.hang1.create_image(200,200,image=self.photo9)
        elif self.counter ==10:
            self.hang1.create_image(200,200,image=self.photo10)
        else:
            pass
        
    def reset(self, master):
        """Startar om spelet från början."""
        self.lst = []
        self.btndct = {}
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.fetch()
        self.buttonize()
        self.textboxes()
        self.mainframe
        self.counter = 1
        self.hang1 = Canvas(self.mainframe,width=400, height=400)
        self.hang1.pack()        
        self.HangTheMan()
        self.pack(fill=BOTH,expand=1)
        self.life = 9
        self.kvar = len(self.word)        
        master.minsize(width=1024,height=768)     
             
    def fetch(self):
        """Läser in listan med ord och väljer ut ett slumpmässigt."""
        corpus = open('corpus2.txt')
        lines = corpus.readlines()
        corpus.close()
        word = lines[randint(0, len(lines) - 1)].rstrip('\r\n')
        word = word.upper()
        self.word = word
        
    def update(self):
        """Uppdaterar spelets tillstånd beroende på rätt eller fel gissning."""
        if self.life <= 0:
            self.gameloss()        
        elif self.kvar <= 0:
            self.gamewin()            
        else:
            pass
        
    def kvarmod(self, mod):
        """Minskar hur många rätt gissningar som är kvar tills man vinner."""
        self.kvar -= mod
        
    def lifemod(self, mod):
        """Minskar hur många fel man kan ha tills man förlorar."""
        self.life -= mod
        
    def gameloss(self):
        """Visar ett meddelande om att man förlorat och frågar om du vill spela igen
        isåfall startas spelet om."""
        if tkMessageBox.askyesno('LOSER!', 'You lose! The word you were looking for was %s... Play again?' % (self.word)):
            self.reset(root)
        else:
            root.destroy()
    
    def gamewin(self):
        """Visar ett meddelande om att man vunnit och frågar om du vill spela igen
        isåfall startas spelet om."""
        if tkMessageBox.askyesno('WINNER!', 'You win! Play again?'):
            self.reset(root)
        else:
            root.destroy()          
        
def callback():
    """Frågar om du verkligen vill stänga av programmet och stänger av programmet om du svarar ja."""
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
        
#Skapar ett root fönster och döper det till Hang Man. Skapar sedan en instans av GUI.
root = Tk()
root.title("Hang Man")
Gui = GUI(root)
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()
