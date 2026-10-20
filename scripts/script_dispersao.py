import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_dispersao():
    df = pd.read_csv("dados/dados_dispersao.csv")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo")
    plt.title("Dispersão: Altura vs Peso por Sexo")
    plt.tight_layout()
    plt.savefig("grafico_dispersao.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_dispersao()