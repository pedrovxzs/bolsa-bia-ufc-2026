import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

# garante a existência da pasta para salvar os resultados
os.makedirs('resultados', exist_ok=True)

df = pd.read_csv('dados/leiturasCartao2.csv')
df['DataHora'] = pd.to_datetime(df['DataHora'], dayfirst=True)

# separando as colunas por categoria para os comparativos
cols_temp = [c for c in df.columns if 'temp' in c.lower()]
cols_umi = [c for c in df.columns if 'umi' in c.lower()]

mapa_legendas = {
    'temp_ext': 'Externo',
    'umi_ext': 'Externo',
    'temp_c2_larva ( s3)': 'C2 Larva', 
    'umi_c2_larva(s3)': 'C2 Larva',
    'vest_temp_c2 (s4)': 'C2 Vest',
    'vest_umic2 (s4)': 'C2 Vest',
    'temp_c3_larva (s5)': 'C3 Larva',
    'umi_c3_larva (s5)': 'C3 Larva',
    'vest_temp_c3 (s6)': 'C3 Vest',
    'vest_umi_c3 s6': 'C3 Vest'
}

def gerar_grafico_comparativo(colunas, titulo_principal, label_y, nome_arquivo):
    plt.figure(figsize=(12, 6))
    
    for col in colunas:
        plt.plot(df['DataHora'], df[col].rolling(window=12,center=True).mean(), label=mapa_legendas.get(col, col), linewidth=1)

    # customização do gráfico
    plt.title(titulo_principal, fontsize=14)
    plt.ylabel(label_y, fontsize=12)
    plt.xlabel("Dia", fontsize=12)
    
    # configuração do Eixo X (Início ao Fim, formato dd/mm)
    ax = plt.gca()
    inicio, fim = df['DataHora'].min(), df['DataHora'].max()
    ax.set_xlim(inicio - pd.Timedelta(hours=15), fim)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # legenda no canto superior direito como no modelo dela
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    
    plt.tight_layout()
    plt.savefig(f'resultados/{nome_arquivo}.png', dpi=300)
    plt.close()

# gerar comparativo de todas as Temperaturas
if cols_temp:
    gerar_grafico_comparativo(
        cols_temp, 
        "Comparativo de Temperatura: Larva, Vestíbulo e Externo", 
        "Temperatura (°C)", 
        "comparativo_temperaturas"
    )

# gerar comparativo de todas as Umidades
if cols_umi:
    gerar_grafico_comparativo(
        cols_umi, 
        "Comparativo de Umidade: Larva, Vestíbulo e Externo", 
        "Umidade (%)", 
        "comparativo_umidades"
    )

print("Gráficos comparativos gerados com sucesso na pasta 'resultados'!")