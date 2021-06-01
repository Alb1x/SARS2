import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
import settings
from Lift import main as Lift
description="Ascenseur dont le bouton choisi ne marche plus au bout d'un temps donné."
class main(Lift):


    def custom_init(self):
        self.description=description

    def Aller5d(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="5d" :
            self.Etages.ind5d.select()
            self.Aller5(_dir='-')

    def Aller4u(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="4u" :
            self.Etages.ind4u.select()
            self.Aller4(_dir='+')

    def Aller4d(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="4d" :
            self.Etages.ind4d.select()
            self.Aller4(_dir='-')

    def Aller3u(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="3u" :
            self.Etages.ind3u.select()
            self.Aller3(_dir='+')

    def Aller3d(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="3d" :
            self.Etages.ind3d.select()
            self.Aller3(_dir='-')

    def Aller2u(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="2u" :
            self.Etages.ind2u.select()
            self.Aller2(_dir='+')

    def Aller2d(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="2d" :
            self.Etages.ind2d.select()
            self.Aller2(_dir='-')

    def Aller1u(self):
        end=time.time()
        if end-settings.start<settings.time_before_breakdown or settings.breakdown_button!="1u" :
            self.Etages.ind1u.select()
            self.Aller1(_dir='+')
