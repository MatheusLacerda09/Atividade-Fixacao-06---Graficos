import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_regressao():
    df = pd.read_csv("dados/dados_regressao.csv")
    plt.figure(figsize=(8, 5))
    sns.regplot(data=df, x="renda_mensal", y="gasto_mensal")
    plt.title("Regressão: Renda Mensal vs Gasto Mensal")
    plt.tight_layout()
    plt.savefig("grafico_regressao.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_regressao()