# Verificação de Estacionariedade em Séries Temporais

O presente trabalho busca, através da utilização da biblioteca [pandas](https://pandas.pydata.org/) e [NumPy](https://numpy.org/), verificar se uma série temporal passada como entrada é ou não estacionária.

## Dados utilizados

Para o estudo, utilizei a série temporal dos valores de fechamento das ações da Amazon, encontradas na plataforma [kaggle](www.kaggle.com).

A série temporal utilizada será datada entre os períodos **01/01/2016** e **31/12/2016**.

A seguir, um gráfico contendo a representação da série temporal:

![time series](https://github.com/rubensborrasca/estacionariedade-series-temporais/graphs/time-series.png)

## Para que estudar a estacionariedade de uma série?

Uma série temporal estacionária pode ser considerada como um processo estocástico. Isso é relevante na hora de tratar de predições de séries temporais.

Para utilizar um método auto-regressivo de previsão _(AR)_, por exemplo, é necessário que a série em questão seja estacionária. Portanto, através do teste deste algoritmo, pode-se verificar a utilidade (ou não) de _AR_ em _forecastings_ da série temporal passada como entrada.

## Uso do algorimto

Para utilizar este algoritmo, primeiro inseri o _dataset_ no programa. No caso, utilizei a biblioteca _pandas_ para importar o arquivo _.csv_ e transformá-lo em um _DataFrame_ no programa.

Após, implementei 2 testes conhecidos de verificação de estacionariedade em séries temporais: o de **raíz unitária** e **Dickey-Fueller**.

Se ambos os testes retornam positivos para estacionariedade, ao final da execução do programa, aparecerá uma mensagem ao usuário indicando.