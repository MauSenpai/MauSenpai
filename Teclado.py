"""
ENGLISH:
This code is a example to make a number keyboard with OOP and Tkinter in Python

SPANISH:
Este codigo es un ejemplo de como hacer un teclado numerico con POO y Tkinter 
en Python

Autor: MauSenpai
"""


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

numero = ""
   
class App:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0,0)
        self.master.title("Teclado")
        self.master.geometry("200x230")
        
        frm = tk.Frame(self.master, width=360, height=50)
        frm.pack(pady=5, padx=5, side="top")
        
        self.numerolbl = tk.Label(frm, text="", font="Arial 13", bg="White", width=20)
        self.numerolbl.grid(row=0, column=0, columnspan=2)
        
        
        frm3 = tk.Frame(self.master, width=360, height=300, bg="Gray")
        frm3.pack(pady=5, padx=5, side="top")
        
        self.boton0 = tk.Button(frm3, text = "0", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("0"))
        self.boton0.grid(row=0, column=0,pady=5, padx=5)
        
        self.boton1 = tk.Button(frm3, text = "1", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("1"))
        self.boton1.grid(row=0, column=1,pady=5, padx=5)
        
        self.boton2 = tk.Button(frm3, text = "2", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("2"))
        self.boton2.grid(row=0, column=2,pady=5, padx=5)
        
        self.boton3 = tk.Button(frm3, text = "3", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("3"))
        self.boton3.grid(row=0, column=3,pady=5, padx=5)
        
        self.boton4 = tk.Button(frm3, text = "4", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("4"))
        self.boton4.grid(row=1, column=0,pady=5, padx=5)
        
        self.boton5 = tk.Button(frm3, text = "5", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("5"))
        self.boton5.grid(row=1, column=1,pady=5, padx=5)
        
        self.boton6 = tk.Button(frm3, text = "6", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("6"))
        self.boton6.grid(row=1, column=2,pady=5, padx=5)
        
        self.boton7 = tk.Button(frm3, text = "7", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("7"))
        self.boton7.grid(row=1, column=3,pady=5, padx=5)
        
        self.boton8 = tk.Button(frm3, text = "8", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("8"))
        self.boton8.grid(row=2, column=0,pady=5, padx=5)
        
        self.boton9 = tk.Button(frm3, text = "9", font = "Arial 12", width=3, height=2, command=lambda *arg: self.presionaBoton("9"))
        self.boton9.grid(row=2, column=1,pady=5, padx=5)
        
        self.borra = tk.Button(frm3, text = "<---", font = "Arial 12", command=lambda *arg: self.presionaBoton("<---"))
        self.borra.grid(row=2, column=2, pady=5, padx=5)
        
        self.enter = tk.Button(frm3, text = "Enter", font = "Arial 12", command=lambda *arg: self.presionaBoton("entra"))
        self.enter.grid(row=2, column=3, pady=5, padx=5)
        
    def presionaBoton(self, num):
        global numero
        
        if num == "<---":
            try:
                numero = numero[:-1]
            except:
                messagebox.showinfo(message="No hay nada que borrar", title="Alerta")
            
        elif num=="entra":
            numero = ""
            
        else:
            numero = numero + num
            
        self.numerolbl.config(text=numero)

        
root=tk.Tk()
app=App(root)
root.mainloop()