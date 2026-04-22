import pandas as pd

# ler os dados do arquivo CSV
df = pd.read_csv('data/leiturasCartao2.csv')

# convertendo a coluna de data para o formato datetime e garantindo que o dia seja interpretado corretamente conforme o formato brasileiro (dd/mm/yyyy)
df['DataHora'] = pd.to_datetime(df['DataHora'], dayfirst=True)

colunas_sensores = [col for col in df.columns if col != 'DataHora']

# calculando as métricas estatísticas para cada coluna 
dados = df[colunas_sensores].agg(['mean', 'median', 'min', 'max', 'std']).T

# calculando a moda e pegando apenas o primeiro valor caso haja mais de uma moda
dados['mode'] = [df[col].mode().iloc[0] for col in colunas_sensores]

ordenacao = ['mean', 'median', 'mode', 'min', 'max', 'std']
dados = dados[ordenacao]

# renomeando para algo mais legível
dados.columns = ['média', 'mediana', 'moda','mínimo', 'máximo', 'desvio padrão']

# exibindo as métricas calculadas
print("\n                         --- Métricas ---")

print(dados)
 
# transformando os dados em um arquivo CSV para análise posterior
dados.to_csv('metricas_base.csv')