import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_barras():
    df = pd.read_csv("dados/dados_barras.csv")
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao")
    plt.title("Vendas Médias por Categoria e Região")
    plt.tight_layout()
    plt.savefig("grafico_barras.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_barras()