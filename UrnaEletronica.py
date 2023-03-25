class UrnaEletronica:
    def __init__(self):
        self.candidatos = [ {"nome_candidato": "Rafaela" , "partido": "A"}, 
                            {"nome_candidato": "Adriana" , "partido": "B"}]

    def exibe_candidatos(self):
        for candidatos in self.candidatos:
            print(candidatos.get("nome_candidato"))
            print(candidatos.get("partido"))
    
    def inserir_candidato(self, nome_candidato, partido):
        self.candidatos.append({"nome_candidato": nome_candidato, "partido": partido}) 

    def remover_ultimo_candidato(self):
        self.candidatos.pop()
    
    def atualizar_candidato(self, index, chave, valor): 
        try:
            self.candidatos[index][chave]=valor 
        except IndexError:
            print(f"Indice invalido: {index}")
