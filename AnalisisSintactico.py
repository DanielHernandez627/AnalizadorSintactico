from tkinter import *
from tkinter import messagebox as MessageBox

#Inicio configuracion grafica
window = Tk()
window.title('Analizador sintactico')
window.geometry('700x600')
window['bg'] = "#D2D1D1"
lb1 = Label(window,text="Ingrese la oracion tokenizada")
lb1.grid(column=0,row=0)
lb1.place(x=120,y=35, anchor="center")
lb1['bg'] = "#D2D1D1"

#Fin configuracion grafica


def run():
    window.mainloop()


if __name__ == '__main__':
    run()