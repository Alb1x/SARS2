import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur où lors d'appuis successifs sur <<>>, le temps d'ouverture des portes augmente."
class main(Lift):

    def custom_init(self):
        self.description=description

    #Ouvre la porte si l'ascenseur est à l'arrêt
    def Ouvrir(self):
        if self.curMouvement=='0':
            self.target.insert(0,self.CurEtage)
        if self.curMouvement=='p':
            self.CurTempoPortes-=30

