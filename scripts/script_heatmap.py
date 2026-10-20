import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_heatmap():
    df = pd.read_csv("dados/dados_heatmap.csv")
    # Pivotando os dados para o formato matricial exigido pelo heatmap
    heat_pivot = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
    
    plt.figure(figsize=(8, 5))
    sns.heatmap(heat_pivot, annot=True, cmap="YlGnBu", fmt="g")
    plt.title("Heatmap: Movimento de Clientes por Dia e Horário")
    plt.tight_layout()
    plt.savefig("grafico_heatmap.png")
    plt.show()

if __name__ == "__main__":
    gerar_heatmap()