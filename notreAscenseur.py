#!/opt/local/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import time
import sys
import os
from random import randint

import threading

globstop = 0

class MyTimer:
    global globstop
    
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo
    
    def _run(self):
        if globstop :
            self.exit()
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
    
    def start(self):
        
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
    
    def stop(self):
        self._timer.cancel()


class Lift:
    def __init__(self, master):
        self.master = master
        self.master.geometry("170x160")

        self.CreerEtage()
        self.CreerElevator()
        self.master.iconbitmap("elevator.ico")
        self.Etages.master.iconbitmap("elevator.ico")
        self.Elevator.master.iconbitmap("elevator.ico")

        self.buttonA = tk.Button(self.master, text = 'Alarm')
        self.buttonA.pack(fill=tk.X)

        self.button5 = tk.Button(self.master, text = '5',command=self.Aller5)
        self.button5.pack(fill=tk.X)
        self.button4 = tk.Button(self.master, text = '4',command=self.Aller4)
        self.button4.pack(fill='x')
        self.button3 = tk.Button(self.master, text = '3',command=self.Aller3)
        self.button3.pack(fill='x')
        self.button2 = tk.Button(self.master, text = '2',command=self.Aller2)
        self.button2.pack(fill='x')
        self.button1 = tk.Button(self.master, text = '1',command=self.Aller1)
        self.button1.pack(fill='x')
        
        
        self.CurTempo=0
        self.master.title('ascenseur')
        self.CurEtage=1
        self.curMouvement='0'
        self.target=[1]
       
    def Aller5d(self):
        self.Etages.ind5d.select()
        self.Aller5(_dir='-')
        
    def Aller4u(self):
        self.Etages.ind4u.select()
        self.Aller4(_dir='+')
        
    def Aller4d(self):
        self.Etages.ind4d.select()
        self.Aller4(_dir='-')
        
    def Aller3u(self):
        self.Etages.ind3u.select()
        self.Aller3(_dir='+')
        
    def Aller3d(self):
        self.Etages.ind3d.select()
        self.Aller3(_dir='-')    
        
    def Aller2u(self):
        self.Etages.ind2u.select()
        self.Aller2(_dir='+')
        
    def Aller2d(self):
        self.Etages.ind2d.select()
        self.Aller2(_dir='-')   
    
    def Aller1u(self):
        self.Etages.ind1u.select()
        self.Aller1(_dir='+')
        
        
    def Aller5(self,_dir='n'):
        if 5 not in self.target:
            self.target.append(5)

    def Aller4(self,_dir='n'):
        if len(self.target)==0:
                self.target.append(4)
                return
                
        if 4<max(self.CurEtage, self.target[0]) and 4>min(self.CurEtage, self.target[0]): # Si sur le chemin
            if _dir==self.curMouvement or _dir=='n': #dans la même direction
                if 4 in self.target:
                    if self.target.index(4)>0:
                        self.target.remove(4)
                    else:
                        return
                self.target.insert(0,4)
                return
                
        for i in range(1,len(self.target)):
            if 4<max(self.target[i-1], self.target[i]) and 4>min(self.target[i-1], self.target[i]):
                temp='-'
                if self.target[i]-self.target[i-1]>0:
                    temp='+'
                if _dir==temp or _dir=='n':
                    if 4 in self.target:
                        if self.target.index(4)>i:
                            self.target.remove(4)
                        else:
                            return
                    self.target.insert(i,4)
                    return
        if 4 not in self.target:
            self.target.append(4)
    
    def Aller3(self,_dir='n'):
        if len(self.target)==0:
                self.target.append(3)
                return
                
        if 3<max(self.CurEtage, self.target[0]) and 3>min(self.CurEtage, self.target[0]): # Si sur le chemin
            if _dir==self.curMouvement or _dir=='n': #dans la même direction
                if 3 in self.target:
                    if self.target.index(3)>0:
                        self.target.remove(3)
                    else:
                        return
                self.target.insert(0,3)
                return
                
        for i in range(1,len(self.target)):
            if 3<max(self.target[i-1], self.target[i]) and 3>min(self.target[i-1], self.target[i]):
                temp='-'
                if self.target[i]-self.target[i-1]>0:
                    temp='+'
                if _dir==temp or _dir=='n':
                    if 3 in self.target:
                        if self.target.index(3)>i:
                            self.target.remove(3)
                        else:
                            return
                    self.target.insert(i,3)
                    return
        if 3 not in self.target:
            self.target.append(3)

    def Aller2(self,_dir='n'):
        if len(self.target)==0:
                self.target.append(2)
                return
                
        if 2<max(self.CurEtage, self.target[0]) and 2>min(self.CurEtage, self.target[0]): # Si sur le chemin
            if _dir==self.curMouvement or _dir=='n': #dans la même direction
                if 2in self.target:
                    if self.target.index(2)>0:
                        self.target.remove(2)
                    else:
                        return
                self.target.insert(0,2)
                return
                
        for i in range(1,len(self.target)):
            if 2<max(self.target[i-1], self.target[i]) and 2>min(self.target[i-1], self.target[i]):
                temp='-'
                if self.target[i]-self.target[i-1]>0:
                    temp='+'
                if _dir==temp or _dir=='n':
                    if 2 in self.target:
                        if self.target.index(2)>i:
                            self.target.remove(2)
                        else:
                            return
                    self.target.insert(i,2)
                    return
        if 2 not in self.target:
            self.target.append(2)

    def Aller1(self,_dir='n'):
        if 1 not in self.target:
            self.target.append(1)

    def turnoff_l(self,etage,_dir):
        if etage==1:
            self.Etages.ind1u.deselect()
        if etage==2:
            self.Etages.ind2u.deselect()
            self.Etages.ind2d.deselect()
        if etage==3:
            self.Etages.ind3u.deselect()
            self.Etages.ind3d.deselect()
        if etage==4:
            self.Etages.ind4u.deselect()
            self.Etages.ind4d.deselect()
        if etage==5:
            self.Etages.ind5d.deselect()

    def CreerEtage(self):
        self.newWindow = tk.Toplevel(self.master)
        self.Etages = Etages(self.newWindow,self)

    def CreerElevator(self):

        self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.newWindow)

    def move(self):
# comment out for exam
        #print (self.curMouvement)
        #print (self.CurEtage)
        #print (self.CurTempo)
        #print (self.target)
        '''
        if self.CurEtage > 5:
            self.CurEtage=5
            self.curMouvement='0'
        if self.CurEtage < 1:
            self.CurEtage=1
            self.curMouvement='0'
        '''
        if self.curMouvement == '+' or self.curMouvement=='-' or self.curMouvement== 'p':
            self.CurTempo=self.CurTempo+1
        if self.CurTempo == 50 or self.CurTempo==0:
            
            if self.curMouvement=='p':
                self.curMouvement='0'
            
            if len(self.target)>0:
                if self.curMouvement=='+':
                    self.CurEtage=self.CurEtage+1
                    if self.CurEtage==self.target[0]:
                        self.turnoff_l(self.CurEtage,self.curMouvement)
                        self.curMouvement='p'
                        self.target.pop(0)
                if self.curMouvement=='-':
                    self.CurEtage=self.CurEtage-1
                    if self.CurEtage==self.target[0]:
                        self.turnoff_l(self.CurEtage,self.curMouvement)
                        self.curMouvement='p'
                        self.target.pop(0)

            self.UpdateColor()
            self.CurTempo=0


        if self.curMouvement=='0':
            if len(self.target)>0:
                if self.CurEtage < self.target[0]:
                    self.curMouvement='+'
                    self.UpdateColor()
                if self.CurEtage >self.target[0]:
                    self.curMouvement='-'
                    self.UpdateColor()
                if self.target[0]==self.CurEtage:
                    self.target.pop(0)
    
                        
    def UpdateColor(self):
#        print "UpdateColor", self.curMouvement, self.CurEtage
        if self.curMouvement=='0':
            if self.CurEtage == 1:
                self.Elevator.Rouge1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Rouge2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Rouge3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Rouge4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Rouge5()

        if self.curMouvement=='p':
            if self.CurEtage == 1:
                self.Elevator.Vert1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Vert2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Vert3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Vert4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Vert5()


        if self.curMouvement=='+':
            if self.CurEtage == 1:
                self.Elevator.Orange1()
                self.Elevator.Bleu2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Orange2()
                self.Elevator.Bleu3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Orange3()
                self.Elevator.Bleu4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Orange4()
                self.Elevator.Bleu5()


        if self.curMouvement=='-':
            if self.CurEtage == 2:
                self.Elevator.Bleu1()
                self.Elevator.Orange2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Bleu2()
                self.Elevator.Orange3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Bleu3()
                self.Elevator.Orange4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Bleu4()
                self.Elevator.Orange5()

    def sortir(self):
        global globstop
        globstop = 1
        sys.exit(1)


class Etages(Lift):
    def __init__(self, master,Lift):
        self.master = master

        self.master.title('Etages')
        
        #print(os.path.dirname(os.path.realpath(__file__)))
        img = tk.PhotoImage(file="on.gif")
       
        '''
        self.button5u=tk.Button(self.frame,text='5 ^',command=Lift.Aller5)
        self.button5u.pack()
        '''
        self.button5d=tk.Button(self.master,text='5 v',command=Lift.Aller5d)
        self.button5d.place(height=30, width=30, x=30,y=0)
        self.ind5d= tk.Checkbutton(self.master,selectimage =img,image=img)
        self.ind5d.place(x=70,y=5)
       
       
        self.button4u=tk.Button(self.master,text='4 ^',command=Lift.Aller4u)
        self.button4u.place(height=30, width=30, x=30,y=30)
        self.ind4u= tk.Checkbutton(self.master,state='disabled')
        self.ind4u.place(x=70,y=35)
        
        self.button4d=tk.Button(self.master,text='4 v',command=Lift.Aller4d)
        self.button4d.place(height=30, width=30, x=30,y=60)
        self.ind4d= tk.Checkbutton(self.master,state='disabled')
        self.ind4d.place(x=70,y=65)


        self.button3u=tk.Button(self.master,text='3 ^',command=Lift.Aller3u)
        self.button3u.place(height=30, width=30, x=30,y=90)
        self.ind3u= tk.Checkbutton(self.master,state='disabled')
        self.ind3u.place(x=70,y=95)
    
        self.button3d=tk.Button(self.master,text='3 v',command=Lift.Aller3d)
        self.button3d.place(height=30, width=30, x=30,y=120)
        self.ind3d= tk.Checkbutton(self.master,state='disabled')
        self.ind3d.place(x=70,y=125)
        

        self.button2u=tk.Button(self.master,text='2 ^',command=Lift.Aller2u)
        self.button2u.place(height=30, width=30, x=30,y=150)
        self.ind2u= tk.Checkbutton(self.master,state='disabled')
        self.ind2u.place(x=70,y=155)
        
        self.button2d=tk.Button(self.master,text='2 v',command=Lift.Aller2d)
        self.button2d.place(height=30, width=30, x=30,y=180)
        self.ind2d= tk.Checkbutton(self.master,state='disabled')
        self.ind2d.place(x=70,y=185)
        
        
        self.button1u=tk.Button(self.master,text='1 ^',command=Lift.Aller1u)
        self.button1u.place(height=30, width=30, x=30,y=210)
        self.ind1u= tk.Checkbutton(self.master,state='disabled')
        self.ind1u.place(x=70,y=215)
        '''
        self.button1d=tk.Button(self.frame,text='1 v',command=Lift.Aller1)
        self.button1d.pack()
        '''
        
        self.master.geometry("100x240")
        #self.master.geometry("+200+200")

    def close_windows(self):
        self.master.destroy()

class Elevator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Position')

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

        self.master.geometry("170x170")

        self.frame.pack()

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



def main(): 
    root = tk.Tk()
    app = Lift(root)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron=MyTimer(0.02,app.move)
    #comment out for debuging
    #Cron=MyTimer(0.1,app.move)
    Cron.start()
    root.mainloop()

if __name__ == '__main__':
    main()
