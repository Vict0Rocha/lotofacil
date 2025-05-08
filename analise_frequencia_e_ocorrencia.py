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

# 1. Quais são os 5 números sorteados mais vezes?
    def mostrar_mais_frequentes(self, quantidade=5):
        print(f"\n{quantidade} números mais sorteados:")
        mais_frequentes = self.frequencias.head(quantidade)
        for numero, frequencia in mais_frequentes.items():
            print(f"Número: {numero}, Frequência: {frequencia}")

# 2. Quais são os 5 números sorteados menos vezes?
    def mostrar_menos_frequentes(self, quantidade=5):
        print(f"\n{quantidade} números menos sorteados:")
        menos_frequentes = self.frequencias.tail(quantidade)
        for numero, frequencia in menos_frequentes.items():
            print(f"Número: {numero}, Frequência: {frequencia}")

# 3. Qual a diferença entre a frequência do número mais comum e do menos comum?
    def mostrar_diferenca_extremos(self):
        numero_mais = self.frequencias.idxmax()
        freq_mais = self.frequencias.max()
        numero_menos = self.frequencias.idxmin()
        freq_menos = self.frequencias.min()
        diferenca = freq_mais - freq_menos

        print(f"\nNúmero mais comum: {numero_mais}, Frequência: {freq_mais}")
        print(f"Número menos comum: {numero_menos}, Frequência: {freq_menos}")
        print(f"Diferença entre eles: {diferenca}")

# 4. Qual número foi sorteado em mais sorteios seguidos? Quantas vezes isso aconteceu?
    def mostrar_maior_sequencia_consecutiva(self):
        sequencias: dict[int, int] = {}

        for numero in self.frequencias.index.tolist():
            maior_seq = 0
            atual_seq = 0

            for sorteio in self.df.loc[:, 'N1':'N15'].values:
                if numero in sorteio:
                    atual_seq += 1
                    maior_seq = max(maior_seq, atual_seq)
                else:
                    atual_seq = 0

            sequencias[int(numero)] = maior_seq  # Garante que a chave é int

        # Evita erro do PyLance usando items()
        numero_mais_sequencias, vezes_seguido = max(
            sequencias.items(), key=lambda item: item[1])

        print(
            f"\nNúmero sorteado mais vezes seguida: {numero_mais_sequencias}")
        print(f"Apareceu {vezes_seguido} vezes seguidas")

# 5. Qual número ficou mais sorteios consecutivos sem aparecer?
    def mostrar_maior_ausencia_consecutiva(self):
        ausencias: dict[int, int] = {}

        for numero in self.frequencias.index.tolist():
            maior_ausencia = 0
            atual_ausencia = 0

            for sorteio in self.df.loc[:, 'N1':'N15'].values:
                if numero not in sorteio:
                    atual_ausencia += 1
                    maior_ausencia = max(maior_ausencia, atual_ausencia)
                else:
                    atual_ausencia = 0

            ausencias[int(numero)] = maior_ausencia

        numero_mais_ausente, vezes_ausente = max(
            ausencias.items(), key=lambda item: item[1])
        print(
            f"\nNúmero que ficou mais sorteios consecutivos sem aparecer: {numero_mais_ausente}")
        print(f"Ficou {vezes_ausente} vezes seguidas ausente.")

# 6. Qual foi a maior sequência de números consecutivos já sorteada?
    def mostrar_maior_sequencia_numeros_consecutivos(self):
        maior_seq_total = 0
        sorteio_referencia = None

        for idx, linha in enumerate(self.df.loc[:, 'N1':'N15'].values, start=1):
            numeros_ordenados = sorted(linha)
            seq_atual = 1
            maior_seq = 1

            for i in range(1, len(numeros_ordenados)):
                if numeros_ordenados[i] == numeros_ordenados[i - 1] + 1:
                    seq_atual += 1
                    maior_seq = max(maior_seq, seq_atual)
                else:
                    seq_atual = 1

            if maior_seq > maior_seq_total:
                maior_seq_total = maior_seq
                sorteio_referencia = idx

        print(
            f"\nMaior sequência de números consecutivos sorteados: {maior_seq_total}")
        print(f"Números: {sorteio_referencia} (no sorteio)")

# 7. Quantos números pares e ímpares aparecem, em média, em cada sorteio?
    def mostrar_media_pares_impares(self):
        totais_pares = 0
        totais_impares = 0
        total_sorteios = len(self.df)

        for linha in self.df.loc[:, 'N1':'N15'].values:
            pares = sum(1 for n in linha if n % 2 == 0)
            impares = 15 - pares  # Sempre 15 números por sorteio
            totais_pares += pares
            totais_impares += impares

        media_pares = totais_pares / total_sorteios
        media_impares = totais_impares / total_sorteios

        print(f"\nMédia de números pares por sorteio: {media_pares:.2f}")
        print(f"Média de números ímpares por sorteio: {media_impares:.2f}")


if __name__ == '__main__':
    analise = Analise(caminho_arquivo)

    analise.mostrar_mais_frequentes()
    print(60*'-')
    analise.mostrar_menos_frequentes()
    print(60*'-')
    analise.mostrar_diferenca_extremos()
    print(60*'-')
    analise.mostrar_maior_sequencia_consecutiva()
    print(60*'-')
    analise.mostrar_maior_ausencia_consecutiva()
    print(60*'-')
    analise.mostrar_maior_sequencia_numeros_consecutivos()
    print(60*'-')
    analise.mostrar_media_pares_impares()
    print(60*'-')
