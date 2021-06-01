import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur qui échange 2 boutons à l'extérieur de l'ascenseur"
class main(Lift):

    def custom_init(self):
        self.description=description

    def Aller5d(self):
        global etages_bug
        self.Etages.ind5d.select()

        if etages_bug[0]==5 or etages_bug[1]==5 :
            if etages_bug[0]==5 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller5(_dir='-')

    def Aller4u(self):
        global etages_bug
        self.Etages.ind4u.select()
        if etages_bug[0]==4 or etages_bug[1]==4 :
            if etages_bug[0]==4 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller4(_dir='+')

    def Aller4d(self):
        global etages_bug
        self.Etages.ind4d.select()
        if etages_bug[0]==4 or etages_bug[1]==4 :
            if etages_bug[0]==4 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller4(_dir='-')

    def Aller3u(self):
        global etages_bug
        self.Etages.ind3u.select()
        if etages_bug[0]==3 or etages_bug[1]==3 :
            if etages_bug[0]==3 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller3(_dir='+')

    def Aller3d(self):
        global etages_bug
        self.Etages.ind3d.select()
        if etages_bug[0]==3 or etages_bug[1]==3 :
            if self.etages_bug[0]==3 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller3(_dir='-')

    def Aller2u(self):
        global etages_bug
        self.Etages.ind2u.select()
        if etages_bug[0]==2 or etages_bug[1]==2 :
            if etages_bug[0]==2 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller2(_dir='+')

    def Aller2d(self):
        global etages_bug
        self.Etages.ind2d.select()
        if etages_bug[0]==2 or etages_bug[1]==2 :
            if self.etages_bug[0]==2 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller2(_dir='-')
    def Aller1u(self):
        global etages_bug
        self.Etages.ind1u.select()
        if etages_bug[0]==1 or etages_bug[1]==1 :
            if etages_bug[0]==1 :
                Aller=getattr(main, "Aller"+str(etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller1(_dir='+')

