import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_linhas():
    df = pd.read_csv("dados/dados_linhas.csv")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="data", y="vendas", hue="loja")
    plt.title("Evolução de Vendas por Loja")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_linhas.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_linhas()