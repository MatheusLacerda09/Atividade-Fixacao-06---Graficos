import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_boxplot():
    df = pd.read_csv("dados/dados_boxplot.csv")
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="departamento", y="salario")
    plt.title("Distribuição de Salários por Departamento")
    plt.tight_layout()
    plt.savefig("grafico_boxplot.png")
    plt.show()

if __name__ == "__main__":
    gerar_boxplot()