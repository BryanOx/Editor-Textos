from tkinter import *
from tkinter import messagebox, filedialog
from io import open

class EditorTextos(object):
    def __init__(self):
        self.root=Tk()
        self.barraMenu=Menu(self.root)
        self.root.config(menu=self.barraMenu)
        try:
            self.root.title(self.fichero)
            
        except:
            self.root.title("Untitled.txt")

        self.archivoMenu=Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label="Nuevo", command=self.nuevo)
        self.archivoMenu.add_command(label="Abrir", command=self.abrir)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Guardar", command=self.guardar)
        self.archivoMenu.add_command(label="Guardar como...", command=self.guardarComo)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Cerrar")
        self.archivoMenu.add_command(label="Salir", command=self.quit)

        self.editarMenu=Menu(self.barraMenu, tearoff=0)
        self.editarMenu.add_command(label="Copiar")
        self.editarMenu.add_command(label="Cortar")
        self.editarMenu.add_command(label="Pegar")

        self.ayudaMenu=Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu.add_command(label="Licencia", command=self.avisoLicencia)
        self.ayudaMenu.add_command(label="Acerca de...", command=self.informacion)

        self.barraMenu.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.barraMenu.add_cascade(label="Editar", menu=self.editarMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)
        
        self.editorTexto=Frame(self.root)
        self.editorTexto.pack(fill="both", expand="True")
        self.editorTexto.config(width="350", height="150")

        self.texto=Text(self.editorTexto)
        self.texto.pack(fill="both", expand="True", side="left")
        self.texto.config(bg="#191919", fg="#35C9FF")

        self.scrollVert=Scrollbar(self.editorTexto, command=self.texto.yview)
        self.scrollVert.pack(fill="both", side="right")
        self.texto.config(yscrollcommand=self.scrollVert.set)

        self.fichero = None

        self.root.mainloop()

    def nuevo(self):
        n=EditorTextos()

    def abrir(self):
        self.fichero=filedialog.askopenfilename(title="Abrir un archivo", filetypes=(("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))
        apertura=open(self.fichero, "r")
        archivoAbierto=apertura.read()
        self.texto.delete(1.0,"end")
        self.texto.insert(1.0, archivoAbierto)
        apertura.close()
        self.root.title(self.fichero.split("/")[- 1])

    def guardar(self):
        #Guardado(self.texto.get("1.0", END))
        try:
            guardado=open(self.fichero, "w")
            guardado.write(self.texto.get("1.0", END))
            guardado.close()
            self.root.title(self.fichero.split("/")[- 1])

        except:
            self.guardarComo()

    def guardarComo(self):
        self.fichero=filedialog.asksaveasfilename(title="Guardar como..", filetypes=(("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))
        guardado=open(self.fichero, "w")
        guardado.write(self.texto.get("1.0", END))
        guardado.close()
        self.root.title(self.fichero)
        
    def avisoLicencia(self):
        messagebox.showwarning("Licencia de editor de texto.", "Licencia de uso libre.\nEspero disfruten este programa.")

    def informacion(self):
        messagebox.showinfo("Procesador blue escense.", "Procesador de texto con apariencia gris y letras en cian.\nPerfecto para amantes de los temas oscuros.\nCreador: Bryan Oxley\nVersion: 1.0")

    def quit(self):
        valor=messagebox.askquestion("Salir", "¿Seguro que deseas salir del programa?")
        if valor=="yes":
            self.root.destroy()

def main():
    x=EditorTextos()

if __name__ == "__main__":
    main()