import sys
sys.path.insert(0, '..')
from notreAscenseur import *
import tkinter as tk
from Lift import main as Lift
description="Ascenseur où les boutons ont une chance sur 5 de ne pas marcher."
class main(Lift):


    def custom_init(self):
        self.description=description

    def Aller5d(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind5d.select()
        self.Aller5(_dir='-')

    def Aller4u(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind4u.select()
        self.Aller4(_dir='+')

    def Aller4d(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind4d.select()
        self.Aller4(_dir='-')

    def Aller3u(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind3u.select()
        self.Aller3(_dir='+')

    def Aller3d(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind3d.select()
        self.Aller3(_dir='-')

    def Aller2u(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind2u.select()
        self.Aller2(_dir='+')

    def Aller2d(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind2d.select()
        self.Aller2(_dir='-')

    def Aller1u(self):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1:
            return
        self.Etages.ind1u.select()
        self.Aller1(_dir='+')


    def Aller5(self,_dir='n'):
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1 and _dir=='n':
            return
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
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1 and _dir=='n':
            return
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
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1 and _dir=='n':
            return
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
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1 and _dir=='n':
            return
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
        #Le bouton ne marche pas 1 fois sur 5
        if randint(1,5)==1 and _dir=='n':
            return
        if self.CurEtage==1:
            self.turnoff_l(1)
            self.Ouvrir()
            return
        if 1 not in self.target:
            if self.CurEtage==2:
                self.target.insert(0,1)
            else:
                self.target.append(1)