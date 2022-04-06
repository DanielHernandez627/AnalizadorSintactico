from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog

#Inicio logica

terminal = ["id","+","*","(",")","$"]
splitToken = []
splitToken2 = []

def browseFiles(): 
    MessageBox.showwarning("Alerta","Cada cadena debe esta seperar por el simbolo |. Ejemplo Id|+|Id")
    rutfichero = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    lb2.configure(text=rutfichero) 

def openfile():
    fichero = open(lb2.cget("text"))
    for i in fichero.readlines():
        return i

def remove_pila(x):
    for t in terminal:
        if x == t or x == "$":
            if x == t:
                return True
            return False

def error():
    MessageBox.showwarning("Alerta","La pila esta vacia")

def analizador():
    token = openfile()
    tokenFinal = token + "|$"
    splitToken = tokenFinal.split("|")
    splitToken2 = tokenFinal.split("|")
    size_pila = len(splitToken)
    for x in splitToken:
        if remove_pila(x) == True:
            splitToken2.remove(x)
        else:
            error()
            break
#Fin logica

#Inicio configuracion grafica
window = Tk()
window.title('Analizador sintactico')
window.geometry('400x500')
window['bg'] = "#D2D1D1"
lb1 = Label(window,text="Seleccione el archivo a leer")
lb1.grid(column=0,row=0)
lb1.place(x=104,y=35, anchor="center")
lb1['bg'] = "#D2D1D1"
lb2 = Label(window)
lb2.grid(column=1,row=1)
lb2.place(x=30,y=50)
lb2['bg'] = "#D2D1D1"
btnsearch = Button(window,text="Buscar",command=browseFiles)
btnsearch.grid(column=0,row=0)
btnsearch.place(x=300,y= 48)
btnverify = Button(window,text="Verificar",command=analizador)
btnverify.grid(column=0,row=0)
btnverify.place(x=300,y=80)
#Fin configuracion grafica

def run():
    window.mainloop()


if __name__ == '__main__':
    run()