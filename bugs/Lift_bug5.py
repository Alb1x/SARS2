import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
import settings
from Lift import main as Lift
description="Un bouton ne fonctionne plus après un certain nombre d'itérations"

break_but = tk.StringVar()
break_but.set("1u")
settings.breakdown_iteration_button=break_but    #bouton en panne après un certain nombre d'utilisations.  
                                                 #Prend ses valeurs dans [1u,2u,3u,4u,2d,3d,4d,5d]
                                     
settings.iterations=5                           #nombre d'itération avant la panne

n = tk.StringVar()
n.set("0")
settings.n=n

n_text = tk.StringVar()
n_text.set("Nombre de fois appuyé / nombre max : 0/"+str(settings.iterations))
settings.n_text=n_text


class main(Lift):
    def custom_init(self):
        self.description=description
        
    def Aller5d(self):
        if settings.breakdown_iteration_button.get()=="5d":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
            
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="5d":
            self.Etages.ind5d.select()
            self.Aller5(_dir='-')
        
    def Aller4u(self):
        if settings.breakdown_iteration_button.get()=="4u":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="4u":
            self.Etages.ind4u.select()
            self.Aller4(_dir='+')
        
    def Aller4d(self):
        if settings.breakdown_iteration_button.get()=="4d":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="4d":
            self.Etages.ind4d.select()
            self.Aller4(_dir='-')
        
    def Aller3u(self):
        if settings.breakdown_iteration_button.get()=="3u":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="3u":
            self.Etages.ind3u.select()
            self.Aller3(_dir='+')
        
    def Aller3d(self):
        if settings.breakdown_iteration_button.get()=="3d":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="3d":
            self.Etages.ind3d.select()
            self.Aller3(_dir='-')    
        
    def Aller2u(self):
        if settings.breakdown_iteration_button.get()=="2u":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="2u":
            self.Etages.ind2u.select()
            self.Aller2(_dir='+')
        
    def Aller2d(self):
        if settings.breakdown_iteration_button.get()=="2d":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.interations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="2d":
            self.Etages.ind2d.select()
            self.Aller2(_dir='-')   
    
    def Aller1u(self):
        if settings.breakdown_iteration_button.get()=="1u":
            n.set(str(int(n.get())+1))
            n_text.set("Nombre de fois appuyé / nombre max : "+n.get()+"/"+str(settings.iterations))
        if int(n.get())<settings.iterations or settings.breakdown_iteration_button.get()!="1u":
            self.Etages.ind1u.select()
            self.Aller1(_dir='+')
    
