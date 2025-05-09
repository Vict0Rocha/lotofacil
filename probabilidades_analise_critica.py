import pandas as pd
from pathlib import Path

# Pegando o caminho absoluto de um arquivo, partindo meu caminho atual.
caminho_arquivo = Path(__file__).parent / 'data/lotofacil.csv'


class Analise:
    def __init__(self, caminho_csv):
        self.df = pd.read_csv(caminho_csv, delimiter=';')
        self.todos_numeros = self.df.loc[:, 'N1':'N15'].melt(value_name="Numero")[
            "Numero"]
        self.frequencias = self.todos_numeros.value_counts()

# 20. Qual a probabilidade de acertar os 15 números com apenas uma aposta?
    def mostrar_probabilidade_acertar_15(self):
        from math import comb
        total_combinacoes = comb(25, 15)
        prob = 1 / total_combinacoes
        print(f"\nProbabilidade de acertar os 15 números com uma aposta:")
        print(f"1 em {total_combinacoes:,} ({prob:.8f})")

# 21. Se você jogar os mesmos números por 100 concursos, quais seriam as chances reais de ganhar?
    def mostrar_chance_ganhar_em_100_concursos(self):
        from math import comb
        prob_1_aposta = 1 / comb(25, 15)
        prob_perder_uma = 1 - prob_1_aposta
        prob_perder_100 = prob_perder_uma ** 100
        prob_ganhar_ao_menos_1 = 1 - prob_perder_100

        print("\nProbabilidade de ganhar pelo menos uma vez em 100 concursos:")
        print(f"{prob_ganhar_ao_menos_1:.6f} ({prob_ganhar_ao_menos_1*100:.4f}%)")


# 22. Qual a probabilidade de um número específico(como o 13) sair em um único sorteio?


    def mostrar_prob_numero_especifico(self, numero=13):
        prob = 15 / 25
        print(
            f"\nProbabilidade de o número {numero} ser sorteado em um concurso:")
        print(f"{prob:.2f} ({prob*100:.2f}%)")


# 23. Por que, mesmo com tantos dados, não é possível prever o próximo resultado com precisão?
'''
Porque cada sorteio é independente e a Lotofácil é um jogo de azar com natureza
aleatória. Apesar de podermos observar frequências passadas, não há uma relação
causal entre um sorteio e o próximo.
'''


# 24. Você acha que algum modelo matemático ou inteligência artificial poderia
# acertar os números da Lotofácil? Por quê?
'''
Não. Porque em jogos verdadeiramente aleatórios, não há nenhum padrão a ser aprendido.
É possivel analisar os dados e auxiliar em decisões, mas não pdemos prever resultados
aleatórios com precisão. 
'''


# 25. Como a ilusão de padrões pode enganar apostadores que confiam em estatísticas?
'''
As pessoas tendem a ver padrões onde não existe. Muitas coias acontecem apenas por 
coincidência.
'''


# 26. Vale a pena apostar com base em análise de dados? O que os dados mostram sobre isso?
'''
Análise de dados pode ajudar a entender o jogo ou escolher combinações mais equilibradas.
Mas não aumenta a chanche real de ganhar, os dados mostram que, estatisticamente,
as chances de acerto são extremamente baixas, mesmo após centenas de concursos.
'''

if __name__ == '__main__':
    analise = Analise(caminho_arquivo)

    analise.mostrar_probabilidade_acertar_15()  # 20
    print(60*'-')
    analise.mostrar_chance_ganhar_em_100_concursos()  # 21
    print(60*'-')
    analise.mostrar_prob_numero_especifico(13)  # 22
    print(60*'-')
