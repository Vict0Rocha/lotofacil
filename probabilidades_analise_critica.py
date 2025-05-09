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


if __name__ == '__main__':
    analise = Analise(caminho_arquivo)

    analise.mostrar_probabilidade_acertar_15()  # 20
    print(60*'-')
    analise.mostrar_chance_ganhar_em_100_concursos()  # 21
    print(60*'-')
    analise.mostrar_prob_numero_especifico(13)  # 22
    print(60*'-')
