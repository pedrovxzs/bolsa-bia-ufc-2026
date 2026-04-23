import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

# Garante que a pasta resultados existe
os.makedirs('resultados', exist_ok=True)


df = pd.read_csv('dados/leiturasCartao2.csv')
df['DataHora'] = pd.to_datetime(df['DataHora'], dayfirst=True)

colunas_sensores = [col for col in df.columns if col != 'DataHora']

# percorrendo as colunas para criar um gráfico para cada 
for col in colunas_sensores:
    plt.figure(figsize=(10, 4))
    
    col_lower = col.lower()

    # identificando o local com base no nome da coluna
    if 'ext' in col_lower:
        local = "Ambiente Externo"
    elif 'larva' in col_lower:
        camera = "C2" if "c2" in col_lower else "C3" if "c3" in col_lower else ""
        local = f"Larva ({camera})"
    elif 'vest' in col_lower:
        camera = "C2" if "c2" in col_lower else "C3" if "c3" in col_lower else ""
        local = f"Vestíbulo ({camera})"
    else:
        local = "Sensor Interno"

    # identificando o tipo de dado com base no nome da coluna
    if 'temp' in col_lower:
        unidade = "Temperatura (°C)"
        tipo = "Temperatura"
    elif 'umi' in col_lower:
        unidade = "Umidade (%)"
        tipo = "Umidade"
    else:
        unidade = "Valor"
        tipo = col
        

    # plotando os dados
    plt.plot(df['DataHora'], df[col], color='steelblue', linewidth=1, label=col)
    
    # customizando o gráfico
    plt.title(f'{tipo} - {local}', fontsize=14)
    plt.xlabel('Dia')
    plt.ylabel(unidade)
    
    # formatando o eixo x para mostrar apenas o dia e mês
    ax = plt.gca()
    ax.set_xlim(df['DataHora'].min(), df['DataHora'].max())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))


    plt.grid(True, linestyle='--', alpha=0.6)
    
    
    # ajustando layout para evitar sobreposição de elementos
    plt.tight_layout()
    
    # salvando o gráfico e nomeando com base no nome da coluna 
    nome_arquivo = f"resultados/grafico_{col.replace(' ', '_').replace('(', '').replace(')', '')}.png"
    plt.savefig(nome_arquivo)
    
    # fecha o gráfico atual para liberar memória e evitar sobreposição
    plt.close()

print("Gráficos gerados e salvos na pasta 'resultados'")