import pandas as pd    
from sklearn.linear_model import LinearRegression
import numpy as np
import datetime

df = pd.read_excel('Dados.xlsx') #importando dados com a blib "pandas"
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%y') # impportando armazenando e convertendo  data no formato dd/mm/yy
df.set_index('Data', inplace=True)

X = np.array(range(len(df))).reshape(-1, 1)   #criando um array x que representa o numero de dias

y = df['Vendas'].values   #armazenando os valores de venda em y

model = LinearRegression().fit(X, y)   #usando linearRegression da bibl skrlearn com os valores de x e y


#previsões para os próximos 5 dias, gerando uma sequência de números inteiros que representam os mesmo
predictions = model.predict(np.array(range(len(df), len(df) + 5)).reshape(-1, 1))  



#imprimindo a previsao dos proximos 5 dias com suas respectivs datas  com uma estrutura de repeticao "for"
print('Previsão de demanda para os próximos 5 dias:')
for i, prediction in enumerate(predictions):
    next_day = (df.index[-1] + datetime.timedelta(days=i+1)).strftime('%d/%m/%y')
    print(f'{next_day}: {prediction:.0f}')



    #imput criado para pausa a tela caso abra via py
input("pressione enter para sair.")
   