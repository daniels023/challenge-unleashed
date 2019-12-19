#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
get_ipython().run_line_magic('matplotlib', 'inline')

xlsx = pd.ExcelFile('dados.xlsx')
df1 = pd.read_excel (xlsx, 'realizado', index_col=0, skiprows=0)
df2 = pd.read_excel (xlsx, 'orcado')
df1_t = df1.T
df1_t.columns = ['mês', 'realizado']
df1_t['realizado'] = pd.to_numeric(df1_t['realizado'])
df = pd.merge(df2, df1_t, on='mês')
df['diff'] = df['orcado'].sub(df['realizado'], axis=0)
df.set_index('mês')
print(df)
df.to_csv('dados_saida_Desafio.csv', index=False)


# In[2]:


df_orcado = df[['orcado']]
df_realizado = df[['realizado']]
df_mes = df[['mês']] 
orcado = df_orcado.T
realizado = df_realizado.T
real = df['realizado'].to_numpy() #y
orc = df['orcado'].to_numpy() #y2
mes = df['mês'].to_numpy() #labels


# In[5]:


x_indexes = np.arange(len(mes))
width = 0.6
plt.figure(figsize=(16, 8))

plt.bar(x_indexes, orc, color="red", label="Orçado")

plt.bar(x_indexes, real, color="#008fd5", label="Realizado")

plt.xticks(ticks=x_indexes, labels=mes)

plt.title("Gráfico Orçamento")
plt.xlabel("Mês")
plt.ylabel("$")

plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
#plt.savefig('plotdata.png')

