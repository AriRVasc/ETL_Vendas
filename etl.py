import pandas as pd

dados_vendas = pd.DataFrame({
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Produto': ['A', 'B', 'A'],
    'Quantidade': [100, 120, 90],
    'Valor': [500.0, 600.0, 450.0]
})

receita_por_produto = dados_vendas.groupby('Produto')['Valor'].sum().reset_index()


receita_por_produto.to_csv('receita_por_produto.csv', index=False)


import matplotlib.pyplot as plt

plt.bar(receita_por_produto['Produto'], receita_por_produto['Valor'])
plt.xlabel('Produto')
plt.ylabel('Receita')
plt.title('Receita por Produto')
plt.show()