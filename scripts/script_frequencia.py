import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_frequencia():
    df = pd.read_csv("dados/dados_frequencia.csv")
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="tipo_atendimento")
    plt.title("Frequência por Tipo de Atendimento")
    plt.tight_layout()
    plt.savefig("grafico_frequencia.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_frequencia()