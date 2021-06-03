import os
import tkinter as tk

def sortir():
    global root
    root.destroy()

def launch_0():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 0"+d)

def launch_1():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 1"+d)

def launch_2():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 2"+d)

def launch_3():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 3"+d)

def launch_4():
    sortir()
    global debug
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 4"+d)

def launch_5():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 5"+d)

def launch_6():
    global debug
    sortir()
    d = "" if debug.get()==0 else " debug"
    os.system("python notreAscenseur.py 6"+d)

def top_frame(root):
    frame = tk.Frame(root)
    button = tk.Button(frame, text="Fonctionnement normal", command=launch_0, activebackground="grey",height=2)
    button.pack(fill="both")
    frame.pack(side="top",fill="both")

def middle_frame(root):
    frame = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)

    button1 = tk.Button(frame, text="Bug n°1", command=launch_1, activebackground="grey",height=2,width=20)
    button2 = tk.Button(frame, text="Bug n°2", command=launch_2, activebackground="grey",height=2,width=20)
    button1.pack(side="left")
    button2.pack(side="left")
    frame.pack(side="top")

    button3 = tk.Button(frame2, text="Bug n°3", command=launch_3, activebackground="grey",height=2,width=20)
    button4 = tk.Button(frame2, text="Bug n°4", command=launch_4, activebackground="grey",height=2,width=20)
    button3.pack(fill="both",side="left")
    button4.pack(fill="both",side="left")
    frame2.pack(side="top")

    button5 = tk.Button(frame3, text="Bug n°5", command=launch_5, activebackground="grey",height=2,width=20)
    button6 = tk.Button(frame3, text="Bug n°6", command=launch_6, activebackground="grey",height=2,width=20)
    button5.pack(side="left")
    button6.pack(side="right")
    frame3.pack(side="top")

def lower_frame(root):
    global debug
    frame= tk.Frame(root)
    debug = tk.IntVar()
    c1 = tk.Checkbutton(frame, text='Activer fenêtre de déboguage',variable=debug, onvalue=1, offvalue=0)
    c1.pack()
    frame.pack()



def main():
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", sortir)
    root.title("Simulation Ascenseur")
    root.geometry("300x200+500+200")
    root.description="Lancement simulation ascenseur"
    root.iconbitmap("elevator.ico")

    top_frame(root)
    middle_frame(root)
    lower_frame(root)







    root.mainloop()



if __name__ == '__main__':
    main()




