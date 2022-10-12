import tkinter as tk
import tkinter.ttk as ttk
import time
from tkinter import messagebox

"""
ENGLISH:
This code is a simulation exercise that records the entry and exit of people 
from a place and saves that information in a txt made with Tkinter

SPANISH:
Este codigo es un ejercicio de simulacion que registra la entrada y la salida
de personas de un local y que guarda esa infomacion en un txt hecho con Tkinter

Author: MauSenpai
"""

contador = 0
registrolista = []
dia = time.strftime("%m/%d/%Y    %H:%M")

class App:
    def __init__(self, master):
        global dia, contador
        self.master = master
        self.master.resizable(0,0)
        self.master.title("Embedded Systems S.A.C")
        self.master.geometry("300x150")
        
        #Frame para Labels
        frm1 = tk.Frame(self.master, width=280, height=100)
        frm1.pack(pady=5)
        
        
        self.fechalbl = tk.Label(frm1, text ="Fecha:", font = "Arial 15")
        self.fechalbl.grid(row=0,column=0, pady=2)
        
        self.fecha = tk.Label(frm1, text =dia, font = "Arial 15")
        self.fecha.grid(row=0,column=1, columnspan=2, pady=2)
        
        self.aforolbl = tk.Label(frm1, text ="Aforo:", font = "Arial 15")
        self.aforolbl.grid(row=2,column=0, pady=2, padx=10)
        
        self.aforo = tk.Label(frm1, text =contador, font = "Arial 15")
        self.aforo.grid(row=2,column=1, columnspan=2, pady=2)
        
        #Frame para botones
        frm2 = tk.Frame(self.master, width=280, height=100)
        frm2.pack(pady=5)
        
        
        self.ingreso = tk.Button(frm2, text="Ingreso", font="Arial 10", command=self.ingreso)
        self.ingreso.grid(row=0, column=0, padx=10, pady=10)
        
        self.salida = tk.Button(frm2, text="Salida", font="Arial 10", command=self.salida)
        self.salida.grid(row=0, column=1, padx=10, pady=10)
        
        self.registro = tk.Button(frm2, text="Registro", font="Arial 10", command=self.registrar)
        self.registro.grid(row=0, column=2, padx=10, pady=10)
       
        
#---------------------------------Funciones------------------------------------ 
    def ingreso(self):
        global contador, registrolista
        
        contador = contador + 1
        
        if contador <= 99:
            dia = time.strftime("%m/%d/%Y    %H:%M")
            dato = f"Fecha: %s    Entra Persona    Estado del contador: %s\n" %(dia, contador)
            registrolista.append(dato)
            self.fecha.config(text = dia)
            self.aforo.config(text = contador)
        
        else: 
            contador = 0
            self.aforo.config(text = "0")

            
    def salida(self):
        global contador, registrolista
         
        if contador > 0:
            contador = contador - 1
            dia = time.strftime("%m/%d/%Y    %H:%M")
            dato = f"Fecha: %s    Sale Persona    Estado del contador: %s\n" %(dia, contador)
            registrolista.append(dato)
            self.fecha.config(text = dia)
            self.aforo.config(text = contador)
             
        else:     
            messagebox.showinfo(message="No hay clientes", title="Alerta")
            contador = 0         
    
    
    def registrar(self):
        with open("Regsitro.txt","a") as archivo:
            for x in registrolista:
                archivo.write(x)
        messagebox.showinfo(message="¡Registro creado!", title="Listo")

root=tk.Tk()
app=App(root)
root.mainloop()