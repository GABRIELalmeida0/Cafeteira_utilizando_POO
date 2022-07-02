import time

class Cafeteira:
    '''Cafeteira'''

    def __init__(self, modelo, cor, time=0, agua=0, cafe=0, ligar=False, funcionando=True):
        self.modelo      = modelo
        self.cor         = cor
        self.time        = time
        self.agua        = agua
        self.cafe        = cafe
        self.ligar       = ligar
        self.funcionando = funcionando

    def ligar_cafeteira(self):
        if self.ligar == True:
            print("A cafeteira já está ligada")
            return
        
        self.ligar = True
        print("Ligando a cafeteira!!!")

    def desligar_cafeteira(self):
        if self.ligar == False:
            print("A cafeteira já está desligada")
            return

        self.ligar = False
        print("Desligando a Cafeteira!!!")

    def botando_cafe(self, colher=1):
        max = 3
        #Delimitando a quantidade de café que pode ser utilizada         
        if self.cafe+colher <= max:
            self.cafe += colher
            print(f"foi colocado {colher}, atualmente tem {self.cafe} colheres")
        else:
            print(f"valor exedido só cabem 3 colheres, atualmente tem {self.cafe} colheres de cafe")

    def botando_agua(self, copo=1):
        max = 3
        #Delimitando a quantidade de água que pode ser utilizada
        if self.agua+copo <= max:
            self.agua += copo
            print(f"foi despejado {copo} copo de água, atualmente tem {self.agua} copos de água")
        else:
            print(f"Quantidade exedida de água, já tem {self.agua} copos de água")

    def fazer_cafe(self):
        if self.cafe and self.agua > 0:
            print("Fazendo café")
            for i in range(1,4):
                print(f"{i:.<10}")
                time.sleep(1)
            print("Café Pronto")
            self.agua = self.cafe = 0


    
caf1 = Cafeteira("modelo", "cor")
caf1.botando_agua()

caf1.botando_agua(2)

caf1.botando_cafe(3)

caf1.fazer_cafe()

caf1.botando_agua(2)

caf1.botando_cafe(3)

caf1.fazer_cafe()




