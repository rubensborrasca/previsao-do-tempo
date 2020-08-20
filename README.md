# Previsão do Tempo

Utilização de cadeias de Markov para tentar estimar o regime de temperaturas na cidade de Krasnodar, na Rússia.

## Cadeias de Markov

Cadeias de Markov são processos estocásticos que trabalham com probabilidades e estados discretos. Mais incisivamente, são processos que ditam a distribuição de probabilidades do próximo estado da medida a partir, exclusivamente, do estado atual, e não dos estados anteriores. Por isso, são chamados de processos “sem memória”.

Neste trabalho pretendo, através da medida de temperatura de um dia, prever qual será o estado de temperatura do dia seguinte, analisando a distribuição de probabilidades fornecida.

## Por que Krasnodar?

O presente trabalho seria eficaz no tratamento de previsão do tempo para qualquer cidade do mundo, desde que fosse adquirido um bom conjunto de dados. Dito isso, optei por escrever minhas conclusões sobre Krasnodar, uma cidade situada no sudoeste da parte europeia da Rússia.

A escolha desta cidade foi feita porque é, há muitos anos, conhecida mundialmente como a cidade com maior amplitude térmica do mundo. No conjunto de dados utilizado para a construção deste trabalho, por exemplo, tivemos registros de temperaturas a -11,3 °C, bem como a 28,2 °C. Como há uma possibilidade muito ampla de temperaturas, é uma boa forma de testar o algoritmo.

## Estados de Temperatura

Dividi o conjunto de dados em 4 possíveis estados de temperatura:

$[-11.35:0] \rightarrow$ **abaixo de zero**

$(0:10] \rightarrow$ **frio**

$(10:20] \rightarrow$ **morno**

$(20:28.18] \rightarrow$ **quente**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

A ideia é que, ao inserir a temperatura do dia de hoje, o algoritmo classifique-a em um dos 4 estados acima, e então consiga estabelecer qual o estado mais provável de temperatura para o dia seguinte.
