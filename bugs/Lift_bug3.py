import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur qui échange 2 boutons à l'extérieur de l'ascenseur"
import settings

clicked1 = tk.StringVar()
clicked1.set("2")
settings.etages_bug.append(clicked1)
clicked2 = tk.StringVar()
clicked2.set("5")
settings.etages_bug.append(clicked2)

class main(Lift):

    def custom_init(self):
        self.description=description

    def Aller5d(self):
        self.Etages.ind5d.select()
        if settings.etages_bug[0].get()=='5' or settings.etages_bug[1].get()=='5' :
            if settings.etages_bug[0].get()=='5' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='-')
        else :
            self.Aller5(_dir='-')

    def Aller4u(self):
        self.Etages.ind4u.select()
        if settings.etages_bug[0].get()=='4' or settings.etages_bug[1].get()=='4' :
            if settings.etages_bug[0].get()=='4' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='+')
        else :
            self.Aller4(_dir='+')

    def Aller4d(self):
        self.Etages.ind4d.select()
        if settings.etages_bug[0].get()=='4' or settings.etages_bug[1].get()=='4' :
            if settings.etages_bug[0].get()=='4' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='-')
        else :
            self.Aller4(_dir='-')

    def Aller3u(self):
        self.Etages.ind3u.select()
        if settings.etages_bug[0].get()=='3' or settings.etages_bug[1].get()=='3' :
            if settings.etages_bug[0].get()=='3' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='+')
        else :
            self.Aller3(_dir='+')

    def Aller3d(self):
        self.Etages.ind3d.select()
        if settings.etages_bug[0].get()=='3' or settings.etages_bug[1].get()=='3' :
            if settings.etages_bug[0].get()=='3' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='-')
        else :
            self.Aller3(_dir='-')

    def Aller2u(self):
        self.Etages.ind2u.select()
        if settings.etages_bug[0].get()=='2' or settings.etages_bug[1].get()=='2' :
            if settings.etages_bug[0].get()=='2' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='+')
        else :
            self.Aller2(_dir='+')

    def Aller2d(self):
        self.Etages.ind2d.select()
        if settings.etages_bug[0].get()=='2' or settings.etages_bug[1].get()=='2' :
            if settings.etages_bug[0].get()=='2':
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='-')
        else :
            self.Aller2(_dir='-')

    def Aller1u(self):
        self.Etages.ind1u.select()
        if settings.etages_bug[0].get()=='1' or settings.etages_bug[1].get()=='1' :
            if settings.etages_bug[0].get()=='1' :
                Aller=getattr(main, "Aller"+settings.etages_bug[1].get())
            else :
                Aller=getattr(main, "Aller"+settings.etages_bug[0].get())
            Aller(self,_dir='+')
        else :
            self.Aller1(_dir='+')

