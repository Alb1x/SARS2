import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
class main(Lift):
    Lift.description2="Ascenseur dont le bouton choisi ne marche plus au bout d'un temps donné."

    def custom_init(self):
        self.description=main.description2

    def Aller5d(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="5d" :
            self.Etages.ind5d.select()
            self.Aller5(_dir='-')

    def Aller4u(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="4u" :
            self.Etages.ind4u.select()
            self.Aller4(_dir='+')

    def Aller4d(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="4d" :
            self.Etages.ind4d.select()
            self.Aller4(_dir='-')

    def Aller3u(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="3u" :
            self.Etages.ind3u.select()
            self.Aller3(_dir='+')

    def Aller3d(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="3d" :
            self.Etages.ind3d.select()
            self.Aller3(_dir='-')

    def Aller2u(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="2u" :
            self.Etages.ind2u.select()
            self.Aller2(_dir='+')

    def Aller2d(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="2d" :
            self.Etages.ind2d.select()
            self.Aller2(_dir='-')

    def Aller1u(self):
        global start
        global breakdown_button
        end=time.time()
        if end-start<time_before_breakdown or breakdown_button!="1u" :
            self.Etages.ind1u.select()
            self.Aller1(_dir='+')
