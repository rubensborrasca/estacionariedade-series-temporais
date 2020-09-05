import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Importando os dados de um arquivo .csv denominado "Dados Amazon.csv"
"""
filename = "Dados Amazon.csv"
inicial_date = pd.to_datetime("2016-01-01") #Data inicial onde começa a pegar a série temporal
end_date = pd.to_datetime("2016-12-31") #Data final onde termina de pegar a série temporal


amzn = pd.read_csv(filename) #Importação dos dados para um dataframe do pandas
amzn['Date'] = pd.to_datetime(amzn['Date']) #Conversão da coluna 'Date' do dataset para formato de data.

amzn = amzn[(amzn['Date'] >= inicial_date) & (amzn['Date'] <= end_date)] #Corta o dataframe só para o pedaço de interesse

"""
Quando se trabalha com séries temporais, é sempre bom visualizá-las. Portanto, salvarei na pasta 'graphs' uma imagem
com a série temporal plotada num gráfico.
"""
plt.figure(figsize=(10,6))
plt.title("Valores de fechamento das ações da Amazon entre "+str(inicial_date.date().strftime('%d/%m/%y'))+" e "+str(end_date.date().strftime('%d/%m/%y')), fontsize=16, fontweight='bold')
plt.ylabel("Fechamento ($)",fontsize=12, style='italic')
plt.xlabel("Data",fontsize=12, style='italic')
plt.plot_date(x='Date',y='Close',fmt='-',data=amzn, color='darkred', label='Amazon')
plt.legend(loc='lower right')
#plt.show()
plt.savefig('graphs/time-series.png')


#########################################
#        TESTE DA RAÍZ UNITÁRIA         #
#########################################
"""
O teste da raíz unitária busca fazer uma regressão linear do tipo y = ax+b entre os valores da série para o tempo t = T e
t = T - 1. A partir disso, o coeficiente a nos diz se a série é ou não estacionária. Se o seu módulo for menor do que 1,
a série temporal é estacionária; Se for menor, não é.
"""

#Primeiro, criei uma função que retorna os coeficientes de uma regressão linear, recebendo como input os valores de
#x e y.

def reg_lin(x,y):          # y = ax + b
    x_arr = np.array(x) #Converte o vetor x em um numpy array
    y_arr = np.array(y) #Converte o vetor y em um numpy array
    x_media = x_arr.mean() #Arranja a média de x
    y_media = y_arr.mean() #Arranja a média de y
    var1 = sum((x_arr - x_media)*(y_arr - y_media))
    var2 = sum((x_arr - x_media)**2)

    a = var1/var2
    b = y_media - a*x_media
    return a,b

x_raizun = amzn['Close'].shift(1)[1:] #Valores da série em T-1
y_raizun = amzn['Close'][1:] #Valores da série em T
raizun = False #Variável booleana que dirá se o teste da raíz unitária retornou positivo ou negativo
a,b = reg_lin(x_raizun,y_raizun)

print("#########################################")
print("#  Resultado do teste da Raiz Unitária  #")
print("#########################################")
if abs(a) <= 1:
    print("A série temporal é estacionária!")
    print("coeficiente a =",a)
    raizun = True
else:
    print("A série temporal não é estacionária.")
    print("coeficente a =",b)

print("\n\n\n")
#########################################
#       TESTE DE DICKEY-FUELLER         #
#########################################
"""
Para o teste de Dickey-Fueller, ao fazer uma regressão do tipo 𝛽𝑥+𝜖 entre os valores da série temporal 𝑦 
e suas respectivas diferenças Δ𝑦,o valor do coeficiente angular 𝛽 deve ser menor que 0 para a série ser
considerada estacionária.
"""

diff_serie = np.array(amzn['Close'].diff())  #Variável que estoca o valor das diferenças da série temporal
x_dickfu = np.array(amzn['Close'])   #Variável que estoca os valores da série temporal
y_dickfu = np.delete(diff_serie,0)  #Retirando o nan que fica nas diferenças
x_dickfu = np.delete(x_dickfu,len(x_dickfu)-1)  #Retirando o último valor da série

dickey_fueller = False #Variável booleana que dirá se o teste de dickey-fueller retornou positivo ou negativo

beta,epsilon = reg_lin(x_dickfu,y_dickfu)

print("##########################################")
print("#  Resultado do teste de Dickey-Fueller  #")
print("##########################################")
if beta < 0:
    print("A série temporal é estacionária!")
    print("coeficiente beta =",beta)
    dickey_fueller = True
else:
    print("A série temporal não é estacionária.")
    print("coeficente beta =",beta)

print("\n\n\n")
########################################
#    COMPARAÇÃO ENTRE OS 2 TESTES      #
########################################
"""
Por último, comparei o resultado dos 2 testes. Caso ambos retornem positivo, pode-se assumir que a série
é estacionária.
"""
if (raizun and dickey_fueller):
    print("A série temporal é estacionária em ambos os testes!")
else:
    print("A série temporal não é estacionária.")

