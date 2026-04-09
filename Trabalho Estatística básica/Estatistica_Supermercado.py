import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Leitura de Dados
df = pd.read_csv("MODULO7_PROJETOFINAL_BASE_SUPERMERCADO - MODULO7_PROJETOFINAL_BASE_SUPERMERCADO (1).csv.csv", delimiter= ',')

# Visão de colunas
print(df.columns)

# Tratamento de Dados
df.columns = df.columns.str.strip()
df['Categoria'] = df['Categoria'].str.strip()

df['Preco_Normal'] = pd.to_numeric(df['Preco_Normal'], errors='coerce')
df['Desconto'] = pd.to_numeric(df['Desconto'], errors='coerce')

# Média e Mediana
media= df.groupby('Categoria')['Preco_Normal'].mean()
mediana = df.groupby('Categoria')['Preco_Normal'].median()

print("\nMÉDIA\n", media)
print("\nMEDIANA\n", mediana)

# Desvio Padrão
desvio = df.groupby('Categoria')['Preco_Normal'].std().dropna()
print("\nDESVIO PADRÃO\n", desvio)

# Boxplot
categoria_maior_desvio = desvio.idxmax()
print("\nCategoria com maior desvio:", categoria_maior_desvio)

df_filtrado = df[df['Categoria'] == categoria_maior_desvio]

plt.figure()
plt.boxplot(df_filtrado['Preco_Normal'].dropna())
plt.title(f'Boxplot - {categoria_maior_desvio}')
plt.ylabel('Preço Padrão')
plt.show()

# Média de Desconto
media_desconto = df.groupby('Categoria')['Desconto'].mean().reset_index()

plt.figure()
plt.bar(media_desconto['Categoria'], media_desconto['Desconto'])
plt.xticks(rotation=45)
plt.title('Média de desconto por Categoria')
plt.ylabel('Desconto')
plt.show()

# Gráfico Interativo
df_plotly = df.groupby(['Categoria', 'Marca'])['Desconto'].mean().reset_index()

fig = px.treemap(
    df_plotly,
    path=['Categoria', 'Marca'],
    values='Desconto',
    title='Média de desconto por Categoria e Marca'
)
fig.show()