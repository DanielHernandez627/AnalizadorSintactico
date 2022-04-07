from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import json

#Inicio logica

terminal = ["id","+","*","(",")","$"]
terminal_select = ""
splitToken = []
splitToken2 = []
not_terminal = []
not_terminal_select = ""

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

def remove_pila_terminal(x):
    for t in terminal:
        if x == t or x == "$":
            if x == t:
                return True
            return False

def error():
    MessageBox.showwarning("Alerta","La pila esta vacia")

def search_token(token):
    sentece = token.split("|")
    senteceFinal = ""
    for i in sentece:
        senteceFinal = senteceFinal + i
    return senteceFinal

def search_Gramatic(x,ae):
    with open("tablaintroduccion.json","r") as j:
        mydata = json.load(j)
        for data in mydata[ae]:
            return data[x]

def search_Dataterminal(ae):
    with open("tablaintroduccion.json","r") as j:
        mydata = json.load(j)
        for data in mydata[ae]:
            return len(data)
            
def verify_Gramatic(size_terminal,x,ae):
    i = 0
    exit_gramitc = ""
    final_exit = ""
    x_original = x
    while i < size_terminal:
        gramatic_return = search_Gramatic(x,ae)
        for zx in gramatic_return.split("|"): #Este for es para la generacion de salidas
            exit_gramitc = exit_gramitc + zx
        if i == 0:
            final_exit = final_exit + "\n" + x_original + "->" + exit_gramitc
        else:
            final_exit = final_exit + "\n" + x + "->" + exit_gramitc
            
        for z in reversed(gramatic_return.split("|")): #Este for es para la pila
            not_terminal.append(z)
            x = z
        
        lb4["text"] = final_exit
        exit_gramitc = ""
        i = i + 1


def analizador():
    token = openfile()
    lb3['text'] = "Oracion ingresada: "+search_token(token)
    tokenFinal = token + "|$"
    splitToken = tokenFinal.split("|")
    #splitToken2 = tokenFinal.split("|")
    size_pila = len(splitToken)
    for idx,x in enumerate(splitToken):
        if idx == 0:
            not_terminal.append("$")
            not_terminal.append("E")
            not_terminal_select = "E"
            terminal_select =  x
        else:   
            if remove_pila_terminal(not_terminal_select) == True or not_terminal_select == "$":
                if remove_pila_terminal(not_terminal_select) == True:
                    print(not_terminal)
                    #splitToken2.remove(x)
                else:
                    error()
                    break
            else:
                verify_Gramatic(search_Dataterminal(terminal_select),not_terminal_select,terminal_select)
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
lb2 = Label(window) #Ruta del fichero de entrada
lb2.grid(column=1,row=1)
lb2.place(x=30,y=50)
lb2['bg'] = "#D2D1D1"
lb3 = Label(window)
lb3.place(x=35,y=75)
lb3['bg'] = "#D2D1D1"
lb4 = Label(window)
lb4.place(x=30,y=90)
lb4['bg'] = "#D2D1D1"
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