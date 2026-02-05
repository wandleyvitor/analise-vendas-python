import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados
df = pd.read_csv("vendas.csv")

# Converter coluna de data
df["data"] = pd.to_datetime(df["data"])

# Criar coluna de receita
df["receita"] = df["quantidade"] * df["preco_unitario"]

# Mostrar os dados com a nova coluna
print(df)

# Análise: receita por categoria
receita_categoria = df.groupby("categoria")["receita"].sum()

# Gráfico
receita_categoria.plot(kind="bar", title="Receita por Categoria")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.show()
