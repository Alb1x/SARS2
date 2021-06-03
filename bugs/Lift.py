import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import settings
import tkinter as tk

class main:
    def __init__(self, master):
        self.master = master
        self.master.title("Ascenseur")
        self.master.geometry("360x280+500+200")
        self.description="Ascenseur fonctionnel"

        for i in range(3):
            self.master.columnconfigure(i, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame_l= tk.Frame(self.master,width=100, height=210)
        #pour debuguer
        #self.frame_l.config(highlightbackground="black", highlightthickness=1)
        self.button_quit = tk.Button(self.frame_l, text= "Exit", command=self.exit)
        self.button_quit.pack()

        self.CreerElevator()
        self.CreerEtage()
        self.CreerMenuOptions()


        self.master.iconbitmap("elevator.ico")

        self.buttonA = tk.Button(self.frame_l, text = 'Alarm')
        self.buttonA.pack()

        self.button5 = tk.Button(self.frame_l, text = '5',command=self.Aller5)
        self.button5.pack(fill='x')
        self.button4 = tk.Button(self.frame_l, text = '4',command=self.Aller4)
        self.button4.pack(fill='x')
        self.button3 = tk.Button(self.frame_l, text = '3',command=self.Aller3)
        self.button3.pack(fill='x')
        self.button2 = tk.Button(self.frame_l, text = '2',command=self.Aller2)
        self.button2.pack(fill='x')
        self.button1 = tk.Button(self.frame_l, text = '1',command=self.Aller1)
        self.button1.pack(fill='x')
        self.button_ouvrir = tk.Button(self.frame_l, text = '<< >>',command=self.Ouvrir)
        self.button_ouvrir.pack(fill='x')

        self.frame_l.pack_propagate(0)
        self.frame_l.grid(row=0, column=0, padx=(10,0))


        self.CurTempo=0
        self.CurTempoPortes=0
        self.CurEtage=1
        self.curMouvement='0'
        self.target=[]

        self.debug_=0
        self.custom_init()

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
        if self.CurEtage==5:
            self.turnoff_l(5)
            self.Ouvrir()
            return
        if 5 not in self.target:
            if self.CurEtage==4:
                self.target.insert(0,5)
            else:
                self.target.append(5)

    def Aller4(self,_dir='n'):
        if self.CurEtage==4 and self.curMouvement=='0':
            self.turnoff_l(4)
            self.Ouvrir()
            return
        if len(self.target)==0:
                self.target.append(4)
                return

        if 4<max(self.CurEtage, self.target[0]) and 4>min(self.CurEtage, self.target[0]): # Si sur le chemin
            temp='-'
            if self.target[0]-self.CurEtage>0:
                temp='+'
            if _dir==temp or _dir=='n': #dans la même direction
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
        if self.CurEtage==3 and self.curMouvement=='0':
            self.turnoff_l(3)
            self.Ouvrir()
            return
        if len(self.target)==0:
                self.target.append(3)
                return

        if 3<max(self.CurEtage, self.target[0]) and 3>min(self.CurEtage, self.target[0]): # Si sur le chemin
            temp='-'
            if self.target[0]-self.CurEtage>0:
                temp='+'
            if _dir==temp or _dir=='n': #dans la même direction
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
        if self.CurEtage==2 and self.curMouvement=='0':
            self.turnoff_l(2)
            self.Ouvrir()
            return
        if len(self.target)==0:
                self.target.append(2)
                return

        if 2<max(self.CurEtage, self.target[0]) and 2>min(self.CurEtage, self.target[0]): # Si sur le chemin
            temp='-'
            if self.target[0]-self.CurEtage>0:
                temp='+'
            if _dir==temp or _dir=='n': #dans la même direction
                if 2 in self.target:
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
        if self.CurEtage==1:
            self.turnoff_l(1)
            self.Ouvrir()
            return
        if 1 not in self.target:
            if self.CurEtage==2:
                self.target.insert(0,1)
            else:
                self.target.append(1)

    def turnoff_l(self,etage):
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

    #Ouvre la porte si l'ascenseur est à l'arrêt
    def Ouvrir(self):
        if self.curMouvement=='0':
            self.target.insert(0,self.CurEtage)
        if self.curMouvement=='p':
            self.CurTempoPortes=0


    def CreerEtage(self):
        #self.newWindow = tk.Toplevel(self.master)
        self.Etages = Etages(self.master,self)

    def CreerElevator(self):

        #self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.master)

    def CreerMenuOptions(self):
        self.menuG = tk.Menu(self.master)
        self.master.config(menu=self.menuG)
        self.menuG.add_command(label="Options", command=self.CreerOptions)



    def CreerOptions(self):
            self.newWindow = tk.Toplevel(self.master)
            self.Options = Options(self.newWindow)
            settings.option_active = True

    def move(self):
        if self.debug_:
            self.mouv_var.set("Mouvement : "+str(self.curMouvement))
            self.eta_var.set("Etage actuel : "+str(self.CurEtage))
            self.tempo_var.set("Tempo : "+str(self.CurTempo))
            self.tempop_var.set("Tempo portes : "+str(self.CurTempoPortes))
            self.target_var.set("Liste target : "+str(self.target))
        if settings.option_active:
            self.Options.t_porte_var.set("Temps d'ouverture des portes : "+str(settings.t_att_po))
            if settings.n_bug=="4":
                settings.time_passed.set("Temps passé / temps de vie = "+str(int(time.time()-settings.start))+"/"+str(int(settings.time_before_breakdown)))

        if self.CurEtage > 5:
            self.CurEtage=5
            self.curMouvement='0'
        if self.CurEtage < 1:
            self.CurEtage=1
            self.curMouvement='0'

        if self.curMouvement == '+' or self.curMouvement=='-' :
            self.CurTempo+=1

        if self.curMouvement== 'p':
            self.CurTempoPortes+=1


        if self.CurTempoPortes==int(settings.t_att_po/0.02) or self.CurTempoPortes==0:
            if self.curMouvement=='p':
                self.curMouvement='0'
            self.CurTempoPortes=0

        if self.CurTempo == 50 or self.CurTempo==0:

            if len(self.target)>0:
                if self.curMouvement=='+':
                    self.CurEtage=self.CurEtage+1
                    if self.CurEtage==self.target[0]:
                        self.turnoff_l(self.CurEtage)
                        self.curMouvement='p'
                        self.target.pop(0)
                if self.curMouvement=='-':
                    self.CurEtage=self.CurEtage-1
                    if self.CurEtage==self.target[0]:
                        self.turnoff_l(self.CurEtage)
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
                    self.turnoff_l(self.CurEtage)
                    self.curMouvement='p' #ouverture des portes si l'ascenseur est en attente
                    self.target.pop(0)
            self.UpdateColor()

        if self.curMouvement== 'p' and self.target:
            if self.target[0]==self.CurEtage:
                self.turnoff_l(self.CurEtage)
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

    def debug(self):
        self.debug_=1
        self.debugWindow = tk.Toplevel(self.master)
        self.debugWindow.geometry("200x140+220+100")
        self.debugWindow.title("Infos")
        self.debugWindow.iconbitmap("bug.ico")
        self.frame_debug= tk.Frame(self.debugWindow)


        self.mouv_var=tk.StringVar()
        mouv=tk.Label(self.frame_debug,textvariable=self.mouv_var)
        mouv.pack(side="top", expand=True, fill="both")

        self.eta_var=tk.StringVar()
        eta=tk.Label(self.frame_debug,textvariable=self.eta_var)
        eta.pack(side="top", expand=True, fill="both")

        self.tempo_var=tk.StringVar()
        tempo=tk.Label(self.frame_debug,textvariable=self.tempo_var)
        tempo.pack(side="top", expand=True, fill="both")

        self.tempop_var=tk.StringVar()
        tempop=tk.Label(self.frame_debug,textvariable=self.tempop_var)
        tempop.pack(side="top", expand=True, fill="both")

        self.target_var=tk.StringVar()
        ltar=tk.Label(self.frame_debug,textvariable=self.target_var)
        ltar.pack(side="top", expand=True, fill="both")


        self.frame_debug.pack_propagate(0)
        self.frame_debug.pack(fill="both", expand=True)


    def exit(self):
        self.master.destroy()
        settings.globstop= 1

    def sortir(self):
        self.exit()
        sys.exit(1)

    def custom_init(self):
        pass