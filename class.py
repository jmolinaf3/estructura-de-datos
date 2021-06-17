class andres:
    def __init__(self,dato="molina"):
        self.frase=dato

    def usovariable(self):
        edad, _peso = 21, 75
        nombres = "josue molina"
        tipo_sexo = "M"
        civil = True
        print("civil={} y su tipo es:{}".format(civil,type(civil)))

    def mostrar(self):
        print("moatrar")
        print(self.frase)
ejercicio1 = andres()
ejercicio1.usovariable()
print(ejercicio1.frase)
ejercicio1.mostrar()