import pandas as pd
from pathlib import Path
from collections import defaultdict

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

# 8. Qual a frequência de aparição de grupos de 5 números sequenciais
# ou mais que se repetem? Qual grupo mais se repetiu e quantas vezes?
    def mostrar_frequencia_grupos_sequenciais(self):
        grupos: dict[tuple[int, ...], int] = defaultdict(int)

        for linha in self.df.loc[:, 'N1':'N15'].values:
            numeros = sorted(linha)
            grupo = []

            for i in range(len(numeros)):
                if i == 0 or numeros[i] == numeros[i-1] + 1:
                    grupo.append(numeros[i])
                else:
                    if len(grupo) >= 5:
                        grupos[tuple(grupo)] += 1
                    grupo = [numeros[i]]
            if len(grupo) >= 5:
                grupos[tuple(grupo)] += 1

        if grupos:
            grupo_mais_repetido = max(grupos.items(), key=lambda x: x[1])
            print("\nGrupos de 5+ números sequenciais mais repetidos:")
            print(
                f"Grupo: {grupo_mais_repetido[0]}, Repetições: {grupo_mais_repetido[1]}")
        else:
            print("\nNenhum grupo de 5 ou mais números sequenciais foi repetido.")

# 9. Qual sorteio teve mais números ímpares?
    def mostrar_sorteio_com_mais_impares(self):
        max_impares = 0
        sorteio_index = None

        for idx, linha in enumerate(self.df.loc[:, 'N1':'N15'].values, start=1):
            impares = sum(1 for n in linha if n % 2 != 0)
            if impares > max_impares:
                max_impares = impares
                sorteio_index = idx

        print(f"\nSorteio com mais números ímpares: Sorteio {sorteio_index}")
        print(f"Números ímpares: {max_impares}")

# 10. Qual sorteio teve mais números pares?
    def mostrar_sorteio_com_mais_pares(self):
        max_pares = 0
        sorteio_index = None

        for idx, linha in enumerate(self.df.loc[:, 'N1':'N15'].values, start=1):
            pares = sum(1 for n in linha if n % 2 == 0)
            if pares > max_pares:
                max_pares = pares
                sorteio_index = idx

        print(f"\nSorteio com mais números pares: Sorteio {sorteio_index}")
        print(f"Números pares: {max_pares}")

# 11. Quantos concursos tiveram exatamente 8 números pares e 7 ímpares? E quantos tiveram 8 ímpares e 7 pares?
    def contar_concursos_com_distribuicao_pares_impares(self):
        pares_8_impares_7 = 0
        impares_8_pares_7 = 0

        for linha in self.df.loc[:, 'N1':'N15'].values:
            pares = sum(1 for n in linha if n % 2 == 0)
            impares = 15 - pares

            if pares == 8 and impares == 7:
                pares_8_impares_7 += 1
            elif impares == 8 and pares == 7:
                impares_8_pares_7 += 1

        print(f"\nConcursos com 8 pares e 7 ímpares: {pares_8_impares_7}")
        print(f"Concursos com 8 ímpares e 7 pares: {impares_8_pares_7}")

# 12. Qual foi o sorteio com a menor quantidade de números acima de 20?
    def mostrar_sorteio_com_menos_acima_de_20(self):
        menor_qtd = 15  # máximo possível
        sorteio_index = None

        for idx, linha in enumerate(self.df.loc[:, 'N1':'N15'].values, start=1):
            qtd = sum(1 for n in linha if n > 20)
            if qtd < menor_qtd:
                menor_qtd = qtd
                sorteio_index = idx

        print(
            f"\nSorteio com menos números > 20: Concurso {sorteio_index} ({menor_qtd} números)")

# 13. Qual foi o sorteio com a menor quantidade de números abaixo de 5?
    def mostrar_sorteio_com_menos_ate_5(self):
        menor_qtd = 15  # máximo possível
        sorteio_index = None

        for idx, linha in enumerate(self.df.loc[:, 'N1':'N15'].values, start=1):
            qtd = sum(1 for n in linha if n <= 5)
            if qtd < menor_qtd:
                menor_qtd = qtd
                sorteio_index = idx

        print(
            f"\nSorteio com menos números <= 5: Concurso {sorteio_index} ({menor_qtd} números)")

# 14. Quantos números sorteados estão geralmente nas faixas: 01–05, 06–10, 11–15, 16–20 e 21–25?
    def mostrar_media_por_faixa(self):
        faixas = {
            '01-05': range(1, 6),
            '06-10': range(6, 11),
            '11-15': range(11, 16),
            '16-20': range(16, 21),
            '21-25': range(21, 26),
        }
        totais = {faixa: 0 for faixa in faixas}
        total_sorteios = len(self.df)

        for linha in self.df.loc[:, 'N1':'N15'].values:
            for faixa, intervalo in faixas.items():
                totais[faixa] += sum(1 for n in linha if n in intervalo)

        print("\nMédia de números por faixa:")
        for faixa, total in totais.items():
            media = total / total_sorteios
            print(f"{faixa}: {media:.2f}")

# 15. Há uma tendência de sorteios com mais números baixos (01–12) ou altos (13–25)? Justifique com dados.
    def mostrar_tendencia_baixos_ou_altos(self):
        total_baixos = 0  # 01–12
        total_altos = 0   # 13–25
        total_sorteios = len(self.df)

        for linha in self.df.loc[:, 'N1':'N15'].values:
            total_baixos += sum(1 for n in linha if 1 <= n <= 12)
            total_altos += sum(1 for n in linha if 13 <= n <= 25)

        media_baixos = total_baixos / total_sorteios
        media_altos = total_altos / total_sorteios

        print("\nTendência entre números baixos (01–12) e altos (13–25):")
        print(f"Média de números baixos por sorteio: {media_baixos:.2f}")
        print(f"Média de números altos por sorteio: {media_altos:.2f}")

        if media_baixos > media_altos:
            print("→ Há uma leve tendência a sorteios com mais números BAIXOS.")
        elif media_altos > media_baixos:
            print("→ Há uma leve tendência a sorteios com mais números ALTOS.")
        else:
            print("→ Não há tendência clara entre baixos e altos.")


if __name__ == '__main__':
    analise = Analise(caminho_arquivo)

    # analise.mostrar_mais_frequentes()  # 1
    # print(60*'-')
    # analise.mostrar_menos_frequentes()  # 2
    # print(60*'-')
    # analise.mostrar_diferenca_extremos()  # 3
    # print(60*'-')
    # analise.mostrar_maior_sequencia_consecutiva()  # 4
    # print(60*'-')
    # analise.mostrar_maior_ausencia_consecutiva()  # 5
    # print(60*'-')
    # analise.mostrar_maior_sequencia_numeros_consecutivos()  # 6
    # print(60*'-')
    # analise.mostrar_media_pares_impares()  # 7
    # print(60*'-')
    # analise.mostrar_frequencia_grupos_sequenciais()  # 8
    # print(60*'-')
    # analise.mostrar_sorteio_com_mais_impares()  # 9
    # print(60*'-')
    # analise.mostrar_sorteio_com_mais_pares()  # 10
    # print(60*'-')
    # analise.contar_concursos_com_distribuicao_pares_impares()  # 11
    # print(60*'-')
    # analise.mostrar_sorteio_com_menos_acima_de_20()  # 12
    # print(60*'-')
    # analise.mostrar_sorteio_com_menos_ate_5()  # 13
    print(60*'-')
    analise.mostrar_media_por_faixa()  # 14
    print(60*'-')
    analise.mostrar_tendencia_baixos_ou_altos()  # 15
    print(60*'-')
