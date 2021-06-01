#!/opt/local/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import time
import sys
import os
from random import randint
import glob


import threading

import settings
start=time.time()


class MyTimer:
    
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo
    
    def _run(self):
        if settings.globstop :
            sys.exit()
            self.stop()
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
    
    def start(self):
        
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
    
    def stop(self):
        self._timer.cancel()



class Etages:
    def __init__(self, master,Lift):
        self.master = master
        self.frame_e = tk.Frame(self.master,width=100, height=280)
        #pour debuguer
        #self.frame_e.config(highlightbackground="black", highlightthickness=1)

        #self.master.title('Etages')
        
        '''
        self.button5u=tk.Button(self.frame,text='5 ^',command=Lift.Aller5)
        self.button5u.pack()
        '''
        self.button5d=tk.Button(self.frame_e,text='5 v',command=Lift.Aller5d)
        self.button5d.place(height=30, width=30, x=0,y=0)
        self.ind5d= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind5d.place(x=40,y=9)
       
       
        self.button4u=tk.Button(self.frame_e,text='4 ^',command=Lift.Aller4u)
        self.button4u.place(height=30, width=30, x=0,y=40)
        self.ind4u= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind4u.place(x=40,y=49)
        
        self.button4d=tk.Button(self.frame_e,text='4 v',command=Lift.Aller4d)
        self.button4d.place(height=30, width=30, x=0,y=70)
        self.ind4d= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind4d.place(x=40,y=79)


        self.button3u=tk.Button(self.frame_e,text='3 ^',command=Lift.Aller3u)
        self.button3u.place(height=30, width=30, x=0,y=110)
        self.ind3u= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind3u.place(x=40,y=119)
    
        self.button3d=tk.Button(self.frame_e,text='3 v',command=Lift.Aller3d)
        self.button3d.place(height=30, width=30, x=0,y=140)
        self.ind3d= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind3d.place(x=40,y=149)
        

        self.button2u=tk.Button(self.frame_e,text='2 ^',command=Lift.Aller2u)
        self.button2u.place(height=30, width=30, x=0,y=180)
        self.ind2u= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind2u.place(x=40,y=189)
        
        self.button2d=tk.Button(self.frame_e,text='2 v',command=Lift.Aller2d)
        self.button2d.place(height=30, width=30, x=0,y=210)
        self.ind2d= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind2d.place(x=40,y=219)
        
        
        self.button1u=tk.Button(self.frame_e,text='1 ^',command=Lift.Aller1u)
        self.button1u.place(height=30, width=30, x=0,y=250)
        self.ind1u= tk.Checkbutton(self.frame_e,font=("Arial",1),state='disabled', selectcolor="green",indicatoron=0,pady=3,padx=3)
        self.ind1u.place(x=40,y=259)
        '''
        self.button1d=tk.Button(self.frame,text='1 v',command=Lift.Aller1)
        self.button1d.pack()
        '''
        
        self.frame_e.grid(row=0,column=2)
        #self.master.geometry("+200+200")

    def close_windows(self):
        self.master.destroy()

class Elevator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,width=150, height=165)
        #pour debuguer
        #self.frame.config(highlightbackground="black", highlightthickness=1)

        #self.master.title('Position')

        style=ttk.Style()
        style.configure("TButton",padding=(0,5,0,5)) 

        style.configure("Red.TButton",foreground='red')
        style.configure("Blue.TButton",foreground='blue')
        style.configure("Green.TButton",foreground='green')
        style.configure("Orange.TButton",foreground='orange')
        style.configure("Black.Tbutton",foreground='black')
        
        self.button5 = ttk.Button(self.frame, text = '#_5_#')
        self.button5.configure(style="Red.TButton")
        self.button5.pack()

        self.button4 = ttk.Button(self.frame, text = '#_4_#')
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()
 
        self.button3 = ttk.Button(self.frame, text = '#_3_#')
        self.button3.configure(style="Green.TButton") 
        self.button3.pack()

        self.button2 = ttk.Button(self.frame, text = '#_2_#')
        self.button2.pack()
        self.button2.configure(style="Orange.TButton")
        
        self.button1 = ttk.Button(self.frame, text = '#_1_#')
        self.button1.configure(style="Black.TButton")
        self.button1.pack()
        
        self.frame.pack_propagate(0)
        self.frame.grid(row=0,column=1)

    def Rouge5(self):

        self.button5.configure(style="Red.TButton")
        self.button5.pack()

    def Bleu5(self):
    
        self.button5.configure(style="Blue.TButton")
        self.button5.pack()
    
    def Vert5(self):
        
        self.button5.configure(style="Green.TButton")
        self.button5.pack()

    def Orange5(self):
        
        self.button5.configure(style="Orange.TButton")
        self.button5.pack()
    
    def Noir5(self):
        
        self.button5.configure(style="Black.TButton")
        self.button5.pack()


    def Rouge4(self):
    
        self.button4.configure(style="Red.TButton")
        self.button4.pack()

    def Bleu4(self):
    
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()

    def Vert4(self):
    
        self.button4.configure(style="Green.TButton")
        self.button4.pack()

    def Orange4(self):
    
        self.button4.configure(style="Orange.TButton")
        self.button4.pack()

    def Noir4(self):
    
        self.button4.configure(style="Black.TButton")
        self.button4.pack()


    def Rouge3(self):
    
        self.button3.configure(style="Red.TButton")
        self.button3.pack()

    def Bleu3(self):
    
        self.button3.configure(style="Blue.TButton")
        self.button3.pack()

    def Vert3(self):
    
        self.button3.configure(style="Green.TButton")
        self.button3.pack()

    def Orange3(self):
    
        self.button3.configure(style="Orange.TButton")
        self.button3.pack()

    def Noir3(self):
    
        self.button3.configure(style="Black.TButton")
        self.button3.pack()


    def Rouge2(self):
    
        self.button2.configure(style="Red.TButton")
        self.button2.pack()

    def Bleu2(self):
    
        self.button2.configure(style="Blue.TButton")
        self.button2.pack()

    def Vert2(self):
    
        self.button2.configure(style="Green.TButton")
        self.button2.pack()

    def Orange2(self):
    
        self.button2.configure(style="Orange.TButton")
        self.button2.pack()

    def Noir2(self):
    
        self.button2.configure(style="Black.TButton")
        self.button2.pack()

    def Rouge1(self):
        
    
        self.button1.configure(style="Red.TButton")
        self.button1.pack()

    def Bleu1(self):
    
        self.button1.configure(style="Blue.TButton")
        self.button1.pack()

    def Vert1(self):
    
        self.button1.configure(style="Green.TButton")
        self.button1.pack()

    def Orange1(self):
    
        self.button1.configure(style="Orange.TButton")
        self.button1.pack()

    def Noir1(self):
    
        self.button1.configure(style="Black.TButton")
        self.button1.pack()


class Options:
    def __init__(self, master):

        self.master = master
        self.master.title("Options")
        self.master.iconbitmap("opt.ico")
        self.master.geometry("250x250+200+200")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
        
        self.frame_options = tk.Frame(self.master,width=250, height=250)
        
        self.frame_portes = tk.Frame(self.frame_options,width=250, height=50)
        text_portes = tk.Label(self.frame_portes,text="Changer le timer des portes")
        text_portes.pack()
        self.t_porte_var=tk.StringVar()
        self.t_porte_label= tk.Label(self.frame_portes, textvariable=self.t_porte_var)
        self.slide_t_porte = tk.Scale(self.frame_portes, from_=1, to=10, orient="horizontal")
        self.slide_t_v = tk.Button(self.frame_portes, text="Enregistrer", command=self.slide_valid)
        self.t_porte_label.pack()
        self.slide_t_porte.pack()
        self.slide_t_v.pack()
        self.frame_portes.pack()
        self.frame_options.pack()
        if(len(sys.argv) >1):
            if sys.argv[1]=='3':
                self.optionsBug3_1()
                
    def on_closing(self):
        settings.option_active = False
        
    def slide_valid(self):
        settings.t_att_po=self.slide_t_porte.get()
    
    def optionsBug3_1(self):
        options = [
            "1",
            "2",
            "3",
            "4",
            "5",
        ]
        
        clicked = tk.StringVar()
        clicked.set("1")
        drop = tk.OptionMenu( self.master , clicked , *options )
        drop.pack()
    

        
    if(len(sys.argv) >1):
        if sys.argv[1]==3:
           optionsBug3_1()


def main(): 
    print("Wesh")
    root = tk.Tk()
    sys.path.insert(0, './bugs')
    L0=glob.glob("./bugs/*.py")
    L=[]
    for i in range(len(L0)):
        nom=L0[i][7:-3]
        L.append(__import__(nom).main)

    if(len(sys.argv) ==1):
        app=L[0](root)
    else :
        arg=sys.argv[1]
        if(not arg.isdigit()):
            print("L'argument doit être un nombre.")
            sys.exit()
        else:
            n=int(arg)
            if(n<0 or n>=len(L)):
                print("Le nombre doit être compris entre 0 et "+str(len(L)-1)+".")
                sys.exit()
            else:
                app=L[n](root)
    if(len(sys.argv)>2 and sys.argv[2] =="debug"):
        app.debug()
    

    print("Démarrage de l'Ascenseur avec le fonctionnement : ",app.description)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron=MyTimer(0.02,app.move)
    #comment out for debuging
    #Cron=MyTimer(0.1,app.move)
    Cron.start()
    root.mainloop()

if __name__ == '__main__':
    main()
