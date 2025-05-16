class Atleta():
    def __init__(self,peso):
        self.aquecido=False
        self.aposentado=False
        self.peso=peso
    
    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
            print("O atleta agora está aposentado!")
        else:
            print("O atleta já está aposentado!")
    
    def aquecer(self):
        if self.aposentado == True:
            print("O atleta não pode aquecer pois está aposentado")
        elif self.aquecido == True:
            print("O atleta já está aquecido")
        else:
            print("O atleta está aquecendo...")
            self.aquecido = True
        
        
    
class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.correndo= False    
    def correr(self):
        if self.aposentado== True:
            print("Atleta aposentado, ele não pode correr")
        elif self.aquecido==False:
            print("Atleta nao esta aquecido, ele não pode correr")
        elif self.correndo == True:
            print("O atleta já está correndo!")
        else:
            self.correndo=True
            print("o atleta começou a correr!")
            
class Nadador(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.nadando= False
    
    def nadar(self):
        if self.aposentado== True:
            print("Atleta aposentado, ele não pode nadar!")
        elif self.aquecido==False:
            print("Atleta não está aquecido, não está pronto para nadar!")
        elif self.nadando== True:
            print("O atleta já está nadando!")
        else:
            self.nadando=True
            print("O atleta foi nadar")
        
class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.pedalando=False
        
    def pedalar(self):
        if self.aposentado== True:
            print("Atleta aposentado, ele não pode pedalar")
        elif self.aquecido==False:
            print("O atleta não está aquecido, ele não pode pedalar")
        elif self.pedalando==True:
            print("O atleta já está pedalando")
        else:
            self.pedalando=True
            print("o atleta foi pedalar")
            
class TriAtleta(Corredor,Nadador,Ciclista):
        def __init__(self, peso):
            super().__init__(peso)
            self.correndo = False
            self.pedalando = False
            self.nadando = False

        def correr(self):
            if self.pedalando:
                print("O atleta está pedalando e não pode correr!")
            elif self.nadando:
                print("O atleta está nadando e não pode correr!")
            elif self.correndo:
                print("O atleta já está correndo!")
            else:
                self.correndo = True
                self.pedalando = False
                self.nadando = False
                Corredor.correr(self)

        def pedalar(self):
            if self.correndo:
                print("O atleta está correndo e não pode pedalar!")
            elif self.nadando:
                print("O atleta está nadando e não pode pedalar!")
            elif self.pedalando:
                print("O atleta já está pedalando!")
            else:
                self.correndo = False
                self.pedalando = True
                self.nadando = False
                Ciclista.pedalar(self)

        def nadar(self):
            if self.pedalando:
                print("O atleta está pedalando e não pode nadar!")
            elif self.correndo:
                print("O atleta está correndo e não pode nadar!")
            elif self.nadando:
                print("O atleta já está nadando!")
            else:
                self.correndo = False
                self.pedalando = False
                self.nadando = True
                Nadador.nadar(self)