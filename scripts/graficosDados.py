import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv('data/leiturasCartao2.csv')
df['DataHora'] = pd.to_datetime(df['DataHora'], dayfirst=True)

colunas_sensores = [col for col in df.columns if col != 'DataHora']

# percorrendo as colunas para criar um gráfico para cada 
for col in colunas_sensores:
    plt.figure(figsize=(10, 4))
    
    # plotando os dados
    plt.plot(df['DataHora'], df[col], color='steelblue', linewidth=1.5)
    
    # customizando o gráfico
    plt.title(f'Série Temporal: {col}', fontsize=12)
    plt.xlabel('Data e Hora')
    plt.ylabel('Valor Lido')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # rotacionando as datas no eixo X para não ficarem amontoadas
    plt.xticks(rotation=45)
    
    # ajustando layout para evitar sobreposição de elementos
    plt.tight_layout()
    
    # salvando o gráfico e nomeando com base no nome da coluna 
    nome_arquivo = f"resultados/grafico_{col.replace(' ', '_').replace('(', '').replace(')', '')}.png"
    plt.savefig(nome_arquivo)
    
    # fecha o gráfico atual para liberar memória e evitar sobreposição
    plt.close()

print("Gráficos gerados e salvos na pasta 'resultados'")