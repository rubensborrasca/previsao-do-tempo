import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import random

#########################################
#   Código criado por Rubens Borrasca   #
#     Email: r.borrasca22@gmail.com     #
#########################################
"""
O objetivo deste código é pegar a série
temporal com os dados da temperatura, e 
dividí-los em "treino" e "teste". Os dados
treino serão usados para calcular a probabi-
lidade de estados, e os dados de teste serão
usados para testar a eficácia do algoritmo.
"""

# 1º Passo: Importação de dados.

city = "Krasnodar" #Variável que diz qual a cidade a ser estudada.

df = pd.read_csv("GlobalLandTemperaturesByCity.csv")
df_aux = df[(df['City'] == city)]
df_krasnodar = df_aux.dropna() #Este é o dataset com as infos que precisamos

# 2º Passo: Separar treino-teste.

"""
A função abaixo separa o conjunto de treino e teste.
Recebe 2 parâmetros: o dataset que se quer separar (df) e 
a razão entre treino e teste (ratio).
"""

def separa_treino_teste(df,ratio):
    N = int(df.shape[0]*ratio)
    print("Núm. de observacoes:",df.shape[0])
    counter_index = np.arange(df.shape[0] - N,df.shape[0])
    index = np.arange(0, df.shape[0] - N)
    Test = df.iloc[counter_index]
    Train = df.iloc[index]
    print("Divisão completa!")
    print("Tamanho do teste:", len(Test))
    print("Tamanho do treino:", len(Train))
    return Train,Test

treino, teste = separa_treino_teste(df_krasnodar, ratio=0.01)
#O dataset foi dividido em 10% teste e 90% treino.

# 3º Passo: Criar a matriz de transição.
"""
A matriz de transição é responsável por calcular a probabilidade
de transição de um estado para outro.
"""

y = np.array(treino['AverageTemperature']) #Série temporal alocada em y
N = len(y)

#Limites para cada estado de temperatura
minimo = -11.347
abaixo_zero = 0
frio = 10
morno = 20
quente = 28

"""
Função que conta e aloca em uma variável qual o estado do próximo
valor da série temporal. Uso para calcular as probabilidades depois.
"""

def count_prob(y):
    #y é y[i+1]
    aux1,aux2,aux3,aux4 = 0,0,0,0
    if ((y >= minimo) & (y <= abaixo_zero)):
        aux1 = 1
    elif ((y > abaixo_zero) & (y <= frio)):
        aux2 = 1
    elif ((y > frio) & (y <= morno)):
        aux3 = 1
    else:
        aux4 = 1
        
    return aux1,aux2,aux3,aux4

"""
Função responsável por calcular as probabilidades de transição e alocá-las numa matriz,
a chamada Matriz de Transição.
"""

def matriz_transicao(y, minimo, abaixo_zero, frio, morno, quente):
    """
    Contagem para o estado "abaixo de zero". Nesta etapa, calcula-se a probabilidade de transição do estado
    "abaixo de zero" para os outros.
    """
    count_abaixo = 0
    count_frio = 0
    count_morno = 0
    count_quente = 0
    for i in range(N-1):
        if ((y[i] >= minimo) & (y[i] <= abaixo_zero)):  #Checa se a temperatura está no intervalo "abaixo de zero"
            aux1,aux2,aux3,aux4 = count_prob(y[i+1])
            count_abaixo += aux1
            count_frio += aux2
            count_morno += aux3
            count_quente += aux4
    estados_zero = np.array([count_abaixo, count_frio, count_morno, count_quente])
    estados_zero #Este vetor aloca as contagens para cada posição.
    
    """
    Contagem para o estado "frio". Nesta etapa, calcula-se a probabilidade de transição do estado
    "frio" para os outros.
    """

    count_abaixo = 0
    count_frio = 0
    count_morno = 0
    count_quente = 0

    for i in range(N-1):
        if ((y[i] > abaixo_zero) & (y[i] <= frio)):  #Checa se a temperatura está no intervalo "frio"
            aux1,aux2,aux3,aux4 = count_prob(y[i+1])
            count_abaixo += aux1
            count_frio += aux2
            count_morno += aux3
            count_quente += aux4
    estados_frio = np.array([count_abaixo, count_frio, count_morno, count_quente])
    estados_frio #Este vetor aloca as contagens para cada posição.

    """
    Contagem para o estado "morno". Nesta etapa, calcula-se a probabilidade de transição do estado
    "morno" para os outros.
    """

    count_abaixo = 0
    count_frio = 0
    count_morno = 0
    count_quente = 0

    for i in range(N-1):
        if ((y[i] > frio) & (y[i] <= morno)):  #Checa se a temperatura está no intervalo "morno"
            aux1,aux2,aux3,aux4 = count_prob(y[i+1])
            count_abaixo += aux1
            count_frio += aux2
            count_morno += aux3
            count_quente += aux4
    estados_morno = np.array([count_abaixo, count_frio, count_morno, count_quente])
    estados_morno #Este vetor aloca as contagens para cada posição.

    """
    Contagem para o estado "quente". Nesta etapa, calcula-se a probabilidade de transição do estado
    "quente" para os outros.
    """

    count_abaixo = 0
    count_frio = 0
    count_morno = 0
    count_quente = 0

    for i in range(N-1):
        if ((y[i] > morno) & (y[i] <= quente)):  #Checa se a temperatura está no intervalo "quente"
            aux1,aux2,aux3,aux4 = count_prob(y[i+1])
            count_abaixo += aux1
            count_frio += aux2
            count_morno += aux3
            count_quente += aux4
    estados_quente = np.array([count_abaixo, count_frio, count_morno, count_quente])
    estados_quente #Este vetor aloca as contagens para cada posição.

    #Calculando as probabilidades. Para isso, basta dividir as contagens pelo número de ocorrências.
    prob_zero = estados_zero/(sum(estados_zero))
    prob_frio = estados_frio/(sum(estados_frio))
    prob_morno = estados_morno/(sum(estados_morno))
    prob_quente = estados_quente/(sum(estados_quente))

    #Construindo a matriz de probabilidades. Basta "empilhar" os vetores com as probabilidades.
    mat_prob = np.array([prob_zero,prob_frio,prob_morno,prob_quente]) #Matriz 4x4.

    return mat_prob

mat = matriz_transicao(y, minimo,abaixo_zero, frio, morno, quente)

#4º Passo: Prever o estado de temperatura.

"""
A função abaixo recebe uma temperatura e transforma-a em um vetor de estado.
Assim, se estivermos no estado "abaixo de zero", o vetor será [1,0,0,0]; No
estado "frio", será [0,1,0,0], no estado morno, [0,0,1,0] e no estado quente,
[0,0,0,1].
"""
def conv_temp_estado(temp):
    if ((temp >= minimo) & (temp <= abaixo_zero)):
        return np.array([1,0,0,0])
    elif ((temp > abaixo_zero) & (temp <= frio)):
        return np.array([0,1,0,0])
    elif ((temp > frio) & (temp <= morno)):
        return np.array([0,0,1,0])
    else:
        return np.array([0,0,0,1])

"""
A função abaixo converte um vetor de probabilidades (retirado da matriz de transição)
em um vetor de estados.
"""

def conv_prob_estado(prob):
    n = len(prob)
    aux = 0
    idx = 0
    for i in range(n):
        if prob[i] >= aux:
            aux = prob[i]
            idx = i
    estado = np.zeros(n)
    estado[idx] = 1
    return estado

"""
Função que compara o estado de temperatura previsto com o estado de temperatura
do conjunto de testes. É útil na hora de calcular o erro.
"""

def compara_estados(estado_prev, estado_teste):
    iguais = True
    for prev,teste in zip(estado_prev,estado_teste):
        if prev != teste:
            iguais = False
    return iguais

y_teste = np.array(teste['AverageTemperature']) #Array com os dados para teste.
estado_previsto = conv_temp_estado(y[-1]) @ mat #"Primero passo" do algoritmo. Pega-se o último estado para prever o próximo.
estados_teste = [] #Vetor que alocará os estados do conjunto de teste
estados_prev = [] #Vetor que alocará os estados das previsões realizadas
count = 0 #Contador de erros
erro = [] #Vetor que alocará o número de erros por número de previsões. Será útil na hora de plotar.
n_previsoes = 3 #Número de previsões requisitadas.

for temp in y_teste[0:n_previsoes+1]:
    estados_teste.append(conv_temp_estado(temp)) #Converte a temperatura em um estado, de acordo com os intervalos estabelecidos.
    estados_prev.append(conv_prob_estado(estado_previsto)) #Converte a previsão em um estado, de acordo com os intervalos estabelecidos.
    if compara_estados(conv_temp_estado(temp), conv_prob_estado(estado_previsto)): #Checa se houve erro na previsão.
        count = count
    else:
        count += 1
    erro.append(count)
    estado_previsto = estado_previsto @ mat #Realiza a previsão para o próximo dia.

#Plot da figura predict.png
"""plt.xlabel("Número de Previsões", fontweight='bold')
plt.ylabel("Número de erros", fontweight='bold')
plt.title("Relação entre o número de previsões e o erro", fontsize=15)
plt.xticks(np.arange(1,n_previsoes+2, 1))
plt.plot(np.arange(1,n_previsoes+2),erro, color='green', linestyle = '--')
plt.scatter(np.arange(1,n_previsoes+2),erro, color='green')"""
#plt.savefig(r"C:\Users\rborr\Projetos GitHub\previsao-do-tempo\graphs\predict.png")

#################################################################################

y_teste = np.array(teste['AverageTemperature']) #Array com os dados para teste.
estado_previsto = conv_temp_estado(y[-1]) @ mat #"Primero passo" do algoritmo. Pega-se o último estado para prever o próximo.
estados_teste = [] #Vetor que alocará os estados do conjunto de teste
estados_prev = [] #Vetor que alocará os estados das previsões realizadas
count = 0 #Contador de erros
erro = [] #Vetor que alocará o número de erros por número de previsões. Será útil na hora de plotar.
n_previsoes = 3 #Número de previsões requisitadas.

for temp in y_teste:
    estados_teste.append(conv_temp_estado(temp)) #Converte a temperatura em um estado, de acordo com os intervalos estabelecidos.
    estados_prev.append(conv_prob_estado(estado_previsto)) #Converte a previsão em um estado, de acordo com os intervalos estabelecidos.
    if compara_estados(conv_temp_estado(temp), conv_prob_estado(estado_previsto)): #Checa se houve erro na previsão.
        count = count
    else:
        count += 1
    erro.append(count)
    estado_previsto = conv_temp_estado(temp) @ mat #Realiza a previsão para o próximo dia. Nota-se que estamos usando o estado do conjunto de teste, e não a previsão anterior.


#Plot da figura retroativo.png
plt.xlabel("Número de Previsões", fontweight='bold')
plt.ylabel("Número de erros", fontweight='bold')
plt.title("Relação entre o número de previsões e o erro", fontsize=15)
plt.xticks(np.arange(1,len(y_teste)+1, 2))
plt.plot(np.arange(1,len(y_teste)+1),erro, color='green', linestyle = '--')
plt.scatter(np.arange(1,len(y_teste)+1),erro, color='green')
plt.savefig(r"C:\Users\rborr\Projetos GitHub\previsao-do-tempo\graphs\retroalimentado.png")
