#todas as classes foram criadas no mesmo arquivo para facilitar a visualização do exercicio completo (:

class SerVivo():
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_vida = int = pontos_de_vida
        self.pontos_de_ataque = int = pontos_de_ataque

    def consultar_pontos_de_vida(self):
        print(f"Seus pontos de vida: {self.pontos_de_vida}")

    def iniciar_ataque(self, ser_causando_ataque, oponente_atacado):
        dano_causado = ser_causando_ataque.pontos_de_ataque
        if oponente_atacado.pontos_de_vida > 0:
            oponente_atacado.pontos_de_vida -= dano_causado
            if oponente_atacado.pontos_de_vida <= 0:
                print("Você matou seu oponente!")
                print("COMBATE FINALIZADO, VOCÊ É O VENCEDOR!")
            else:
                print("Você atacou seu oponente!")
                print(f"Situação do oponente após o dano: {oponente_atacado.pontos_de_vida} pontos de vida")
                print("COMBATE FINALIZADO!")
        else:
            print("Este ser já está morto. Siga em frente.")
            print("COMBATE FINALIZADO!")

class Personagem(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, nome_do_personagem):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome_do_personagem = str = nome_do_personagem

class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo_de_monstro):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo_de_monstro = str = tipo_de_monstro

class Lobo(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, forca):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.forca = int = forca

class Goblin(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, inteligencia):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.inteligencia = int = inteligencia

#caso de teste
goblin1 = Goblin(30, 20, "medio", 100)
humano_comum = Personagem(40, 20, "harry")
goblin1.iniciar_ataque(goblin1, humano_comum) #deixa o humano com 20 pontos de vida
goblin1.iniciar_ataque(goblin1, humano_comum) #deixa o oponente com 0 pontos de vida (morte)
goblin1.consultar_pontos_de_vida()


