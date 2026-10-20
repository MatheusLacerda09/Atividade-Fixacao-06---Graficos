import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_distribuicao():
    df = pd.read_csv("dados/dados_distribuicao.csv")
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="idade", kde=True)
    plt.title("Distribuição de Idade dos Clientes")
    plt.tight_layout()
    plt.savefig("grafico_distribuicao.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_distribuicao()