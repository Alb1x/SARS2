import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur qui échange 2 boutons à l'extérieur de l'ascenseur"
import settings
class main(Lift):

    def custom_init(self):
        self.description=description

    def Aller5d(self):
        self.Etages.ind5d.select()

        if settings.etages_bug[0]==5 or settings.etages_bug[1]==5 :
            if settings.etages_bug[0]==5 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller5(_dir='-')

    def Aller4u(self):
        self.Etages.ind4u.select()
        if settings.etages_bug[0]==4 or settings.etages_bug[1]==4 :
            if settings.etages_bug[0]==4 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller4(_dir='+')

    def Aller4d(self):
        self.Etages.ind4d.select()
        if settings.etages_bug[0]==4 or settings.etages_bug[1]==4 :
            if settings.etages_bug[0]==4 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller4(_dir='-')

    def Aller3u(self):
        self.Etages.ind3u.select()
        if settings.etages_bug[0]==3 or settings.etages_bug[1]==3 :
            if settings.etages_bug[0]==3 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller3(_dir='+')

    def Aller3d(self):
        self.Etages.ind3d.select()
        if settings.etages_bug[0]==3 or settings.etages_bug[1]==3 :
            if self.settings.etages_bug[0]==3 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller3(_dir='-')

    def Aller2u(self):
        self.Etages.ind2u.select()
        if settings.etages_bug[0]==2 or settings.etages_bug[1]==2 :
            if settings.etages_bug[0]==2 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller2(_dir='+')

    def Aller2d(self):
        self.Etages.ind2d.select()
        if settings.etages_bug[0]==2 or settings.etages_bug[1]==2 :
            if self.settings.etages_bug[0]==2 :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.etages_bug[0]))
            Aller(self,_dir='-')
        else :
            self.Aller2(_dir='-')

    def Aller1u(self):
        self.Etages.ind1u.select()
        if settings.settings.etages_bug[0]==1 or settings.settings.etages_bug[1]==1 :
            if settings.settings.etages_bug[0]==1 :
                Aller=getattr(main, "Aller"+str(settings.settings.etages_bug[1]))
            else :
                Aller=getattr(main, "Aller"+str(settings.settings.etages_bug[0]))
            Aller(self,_dir='+')
        else :
            self.Aller1(_dir='+')

