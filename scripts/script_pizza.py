import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_pizza():
    df = pd.read_csv("dados/dados_pizza.csv")
    plt.figure(figsize=(7, 7))
    plt.pie(df["faturamento"], labels=df["canal_venda"], autopct='%1.1f%%', startangle=140)
    plt.title("Faturamento por Canal de Venda")
    plt.tight_layout()
    plt.savefig("grafico_pizza.png")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_pizza()