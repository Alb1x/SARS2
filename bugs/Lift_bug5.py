import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
import settings
from Lift import main as Lift
description="Un bouton ne fonctionne plus après un certain nombre d'itérations"

#breakdown_iteration_button.get()="2d"      #bouton en panne après un certain nombre d'utilisations.  
                                     #Prend ses valeurs dans [door,1u,2u,3u,4u,2d,3d,4d,5d]
                                     
#iteration=3                          #nombre d'itération avant la panne

class main(Lift):
    def Aller5d(self):
        global n
        if settings.breakdown_iteration_button.get()!="5d":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="5d":
            self.Etages.ind5d.select()
            self.Aller5(_dir='-')
        
    def Aller4u(self):
        if settings.breakdown_iteration_button.get()!="4u":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="4u":
            self.Etages.ind4u.select()
            self.Aller4(_dir='+')
        
    def Aller4d(self):
        if settings.breakdown_iteration_button.get()!="4d":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="4d":
            self.Etages.ind4d.select()
            self.Aller4(_dir='-')
        
    def Aller3u(self):
        if settings.breakdown_iteration_button.get()!="3u":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="3u":
            self.Etages.ind3u.select()
            self.Aller3(_dir='+')
        
    def Aller3d(self):
        if settings.breakdown_iteration_button.get()!="3d":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="3d":
            self.Etages.ind3d.select()
            self.Aller3(_dir='-')    
        
    def Aller2u(self):
        if settings.breakdown_iteration_button.get()!="2u":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="2u":
            self.Etages.ind2u.select()
            self.Aller2(_dir='+')
        
    def Aller2d(self):
        if settings.breakdown_iteration_button.get()!="2d":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="2d":
            self.Etages.ind2d.select()
            self.Aller2(_dir='-')   
    
    def Aller1u(self):
        if settings.breakdown_iteration_button.get()!="1u":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="1u":
            self.Etages.ind1u.select()
            self.Aller1(_dir='+')
    def Ouvrir(self):
        if settings.breakdown_iteration_button.get()!="door":
            n+=1
        if n<settings.iterations or settings.breakdown_iteration_button.get()!="door":
            if self.curMouvement=='0':
                self.target.insert(0,self.CurEtage)
                if self.curMouvement=='p':
                    self.CurTempoPortes=0
