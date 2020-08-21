# Previsão do Tempo

Utilização de cadeias de Markov para tentar estimar o regime de temperaturas na cidade de Krasnodar, na Rússia.

## Cadeias de Markov

Cadeias de Markov são processos estocásticos que trabalham com probabilidades e estados discretos. Mais incisivamente, são processos que ditam a distribuição de probabilidades do próximo estado da medida a partir, exclusivamente, do estado atual, e não dos estados anteriores. Por isso, são chamados de processos “sem memória”.

Neste trabalho pretendo, através da medida de temperatura de um dia, prever qual será o estado de temperatura do dia seguinte, analisando a distribuição de probabilidades fornecida.

## Por que Krasnodar?

O presente trabalho seria eficaz no tratamento de previsão do tempo para qualquer cidade do mundo, desde que fosse adquirido um bom conjunto de dados. Dito isso, optei por escrever minhas conclusões sobre Krasnodar, uma cidade situada no sudoeste da parte europeia da Rússia.

A escolha desta cidade foi feita porque é, há muitos anos, conhecida mundialmente como a cidade com maior amplitude térmica do mundo. No conjunto de dados utilizado para a construção deste trabalho, por exemplo, tivemos registros de temperaturas a -11,3 °C, bem como a 28,2 °C. Como há uma possibilidade muito ampla de temperaturas, é uma boa forma de testar o algoritmo.

## Estados de Temperatura

Dividi o conjunto de dados em 4 possíveis estados de temperatura. São eles **abaixo de zero** (temperatura entre -12 e 0 graus), **frio** (temperatura entre 0 e 10 graus), **morno** (temperatura entre 10 e 20 graus) e **quente** (temperatura entre 20 e 30 graus).

A ideia é que, ao inserir a temperatura do dia de hoje, o algoritmo classifique-a em um dos 4 estados acima, e então consiga estabelecer qual o estado mais provável de temperatura para o dia seguinte.

## Conjunto de dados

O conjunto de dados utilizado foi extraído da plataforma [kaggle](https://www.kaggle.com/), e pode ser encontrado neste repositório, na pasta principal, sob o nome de _"GlobalLandTemperaturesByCity.csv"_. Neste dataset, existem informações de mais de 3400 cidades no mundo.

Sobre a cidade de Krasnodar, temos registros de temperatura de 1743 até agosto de 2013. Ao todo, são 3161 observações registradas no dataset.

## Utilizando o algoritmo para prever temperatura

O algoritmo utilizado para tratar cadeias de Markov não é recomendado para previsões em espaços de tempo muito grandes. Isso ocorre porque, a partir de um determinado número de iterações, entra-se no **estado estacionário**, o que significa que a previsão será sempre a mesma. Portanto, se a intenção for realizar a previsão do tempo meses e meses à frente, este não é o melhor caminho. Uma das figuras presentes na pasta _"/graphs/predict.png"_ mostra que, a partir da 4ª previsão, o programa já erra o estado de temperatura, apesar de acertar todos os outros estados. A ideia do algoritmo, portanto, é que ele prevê muito bem temperaturas nas datas próximas às do dia inicial, mas é limitado para previsões mais longas.

Porém, ainda assim o código pode ser útil. Se você deseja apenas descobrir qual será o estado da temperatura no dia seguinte, este funciona perfeitamente. Realizando um ajuste no algoritmo, pode-se torná-lo _retroalimentado_. Mas o que isso implica?

Simples. Digamos que temos a temperatura de hoje, e precisamos prever a do dia seguinte. O programa faz isso com sucesso, como já foi visto. Agora, se amanhã tivermos a necessidade de prever a temperatura do dia seguinte, o código pode usar o estado de temperatura do dia atual, ao invés do estado de temperatura previsto. Desta forma, evita-se a **propagação de erros** pelo algoritmo, e consegue-se uma precisão maior. O resultado pode ser visto na pasta _"/graphs/retroalimentado.png"_

## Possíveis fontes de erro

Como dito anteriormente, cadeias de Markov não são ideais para fazer previsões de séries temporais. Para isso, recomenda-se métodos como ARIMA, ARMA, AR, MA, entre outros. O objetivo deste projeto foi mostrar uma alternativa, para funções mais rápidas e que não precisem de tanta precisão.

Além disso, a matriz de transição formada foi feita utilizando probabilidades de transição. Mas a forma como estas probabilidades foram encontradas as torna "imprevisíveis". Espera-se que o algoritmo funcione melhor para situações que tenham estados e probabilidades de transição mais bem definidos, como por exemplo a transição de estados de energia de um átomo de hidrogênio.
