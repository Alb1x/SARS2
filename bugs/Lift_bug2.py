import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur où lors d'appuis successifs sur <<>>, le temps d'ouverture des portes augmente."
import settings

class main(Lift):

    def custom_init(self):
        self.description=description

    #Ouvre la porte si l'ascenseur est à l'arrêt
    
    def Ouvrir(self):
        if self.curMouvement=='0':
            self.target.insert(0,self.CurEtage)
        if self.curMouvement=='p':
            # Attention : les portes se ferment quand le timer arrive au max OU quand il arrive à 0
            # Ainsi, si l'on retire plus de temps qu'il n'y en a dans le timer, il s'arretera à 0
            # et les portes se fermeront.
            self.CurTempoPortes -= settings.reduction_time

