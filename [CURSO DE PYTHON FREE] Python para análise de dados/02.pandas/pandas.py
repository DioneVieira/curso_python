import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

print(df)
print(type(df))

print('-' * 200)

print('5 primeiras linhas')
print(df.head())

print('-' * 200)

print('5 últimas linhas')
print(df.tail())

print('-' * 200)

print('quantidade de linhas e colunas')
print(df.shape)

print(df.columns)

print(df.duplicated())

print('-' * 200)

# verifica linhas duplicadas
print(df.duplicated().sum())

df.info()

print('-' * 200)

print('verifica existência de NaN')
print(df.isna().sum())

print('-' * 200)

print('sumário estatístico')
print(df.describe())

print('-' * 200)

print('sumário estatístico - inclusive para as variáveis categóricas')
print(df.describe(include='all'))

print('-' * 200)

print('quantidade de valores únicos em cada coluna')
print(df.nunique())

print('-' * 200)

print('valores únicos')
print(df['parental level of education'].unique())

print('-' * 200)

print('frequência entre os gêneros')
print(df.gender.value_counts())

provas = ['math score', 'reading score', 'writing score']

print(df)

print(df.sort_values(['math score']).reset_index(drop=True))

print('-' * 200)

print('ordena o dataset')
df = df.sort_values(by=provas, ascending=False).reset_index(drop=True)

print(df)

print('-' * 200)

print('coluna com a média das provas')
df['mean'] = df[provas].mean(axis=1)

print(df.head())

print('-' * 200)

print('consulta')
print(df.query('(gender == "male") & (`test preparation course` == "none") & (`math score` >= 70)'))

print(df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)])

print(df.loc[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)])

print('-' * 200)

print('agrupamento - agrupa os dados por gênero e obtém estatísticas descritivas')
print(df.groupby(by='gender')[provas].agg([np.mean, np.median]).T)
