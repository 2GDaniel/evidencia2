class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mayor(self):
        if self.nota>=4:
            print("Eegular.")
        else:
            print("No regular")

#Bloque principal

alumno1 = Alumno()
alumno1.inicializar("Daniel", 3)
alumno1.mostrar()
alumno1.mayor()
print("")
alumno2 = Alumno()
alumno2.inicializar("Manuel", 9)
alumno2.mostrar()
alumno2.mayor()