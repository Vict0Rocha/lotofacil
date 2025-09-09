# 📊 Atividade Prática de Análise de Dados: Lotofácil

## 🎯 Objetivo

Analisar os dados históricos dos resultados da Lotofácil a partir de uma abordagem estatística, investigativa e crítica, promovendo o desenvolvimento de habilidades em interpretação de dados, raciocínio lógico, aplicação de conceitos de probabilidade e pensamento analítico.

---

## 🛠️ Orientações

* Utilize planilhas (Excel, Google Sheets) ou ferramentas de análise como Python, R ou Power BI para consultar os dados.
* As respostas devem ser justificadas com base em evidências extraídas dos dados (gráficos, tabelas, frequências, etc).
* Responda com clareza, organizando as informações de forma lógica e coerente.

---

## 🔢 Análise de Frequência e Ocorrência.

1. Quais são os 5 números sorteados mais vezes?
2. Quais são os 5 números sorteados menos vezes?
3. Qual a diferença entre a frequência do número mais comum e do menos comum?
4. Qual número foi sorteado em mais sorteios seguidos? Quantas vezes isso aconteceu?
5. Qual número ficou mais sorteios consecutivos sem aparecer? Quantas vezes isso aconteceu?
6. Qual foi a maior sequência de números consecutivos já sorteada?
7. Quantos números pares e ímpares aparecem, em média, em cada sorteio?
8. Qual a frequência de aparição de grupos de 5 números sequenciais ou mais que se repetem? Qual grupo mais se repetiu e quantas vezes?
9. Qual sorteio teve mais números ímpares?
10. Qual sorteio teve mais números pares?
11. Quantos concursos tiveram exatamente 8 números pares e 7 ímpares? E quantos tiveram 8 ímpares e 7 pares?
12. Qual foi o sorteio com a menor quantidade de números acima de 20?
13. Qual foi o sorteio com a menor quantidade de números abaixo de 5?
14. Quantos números sorteados estão geralmente nas faixas: 01–05, 06–10, 11–15, 16–20 e 21–25?
15. Há uma tendência de sorteios com mais números baixos (01–12) ou altos (13–25)? Justifique com dados.
⏱️ Temporalidade e Tendência ao Longo do Tempo
16. Nos últimos 100 concursos, algum número aumentou significativamente sua frequência? Qual?
17. Algum número ficou mais de 50 concursos sem ser sorteado? Qual?
18. Quantas vezes cada número apareceu?
19. Quantas e quais as combinações diferentes de 15 números entre 01 e 25 podem ser feitas?

---

## 🎲 Probabilidades e Análise Crítica

20. Qual a probabilidade de acertar os 15 números com apenas uma aposta?
21. Se você jogar os mesmos números por 100 concursos, quais seriam as chances reais de ganhar?
22. Qual a probabilidade de um número específico (como o 13) sair em um único sorteio?
23. Por que, mesmo com tantos dados, não é possível prever o próximo resultado com precisão?
24. Você acha que algum modelo matemático ou inteligência artificial poderia acertar os números da Lotofácil? Por quê?
25. Como a ilusão de padrões pode enganar apostadores que confiam em estatísticas?
26. Vale a pena apostar com base em análise de dados? O que os dados mostram sobre isso?

---

## 🧠 Raciocínio Lógico e Estratégias
27. Se você tivesse que montar uma aposta baseada nos dados analisados, como escolheria os números? Explique sua lógica.
28. Se você eliminar sempre os 5 números que menos saíram até agora, suas chances aumentam? Justifique.
29. É possível montar uma estratégia eficiente com base nos 10 números mais frequentes?
30. É mais eficiente escolher números aleatórios ou usar padrões históricos? Por quê?
31. Se você apostasse apenas em múltiplos de 5 (05, 10, 15, 20, 25), quais seriam suas chances reais de acerto?

---

## ✅ Desafio Extra

Monte um pequeno sistema que:

* Permite o usuário digitar uma combinação de 15 números.
* Calcula quantas vezes essa combinação já foi sorteada (se houver).
* Mostra a média de acertos dessa combinação nos últimos 100 concursos.

---

## 📗 Resposta do 1 ao 19:

1. Cinco números mais sorteados: [(20, 2116), (10, 2106), (25, 2088), (11, 2069), (13, 2050)]
2. Cinco números menos sorteados: [(16, 1925), (8, 1956), (23, 1966), (6, 1967), (17, 1977)]
3. Diferença de frequência (mais comum - menos comum): 191
4. Número com mais sorteios seguidos: 7 (25 vezes)
5. Número com mais sorteios sem aparecer: 19 (12 vezes)
6. Maior sequência consecutiva sorteada: 14 números
7. Média por sorteio: 7.21 pares, 7.79 ímpares
8. Grupos de 5+ números sequenciais repetidos: 98.
Grupo mais repetido: (21, 22, 23, 24, 25) (98 vezes)
9. Sorteio com mais ímpares: Concurso 278 (12 ímpares)
10. Sorteio com mais pares: Concurso 54 (11 pares)
11. Concursos com 8 pares e 7 ímpares: 852
Concursos com 8 ímpares e 7 pares: 1037
12. Sorteio com menos números > 20: Concurso 3049 (0 números)
13. Sorteio com menos números <= 5: Concurso 3283 (0 números)
14. Média de números por faixa:
01-05: 3.01
06-10: 2.98
11-15: 3.03
16-20: 2.98
21-25: 3.00
15. Média de números baixos (01-12): 7.20, altos (13-25): 7.80
Não há tendência clara, pois as médias são próximas, indicando distribuição equilibrada.
16. Número com maior aumento de frequência nos últimos 100 concursos: 1 (aumento relativo: 0.1303)
17. Nenhum número ficou 50 concursos sem ser sorteado, pois 19 ficou no máximo 12 concursos.
18. Cada número apareceu: {1: 2031, 2: 2016, 3: 2030, 4: 2030, 5: 2025, 6: 1967, 7: 1979, 8: 1956, 9: 2012, 10: 2106, 11: 2069, 12: 2021, 13: 2050, 14: 2045, 15: 1996, 16: 1925, 17: 1977, 18: 2011, 19: 2006, 20: 2116, 21: 1994, 22: 2013, 23: 1966, 24: 2046, 25: 2088}
19. Combinações possíveis: 3,268,760
