# Acompanhamento de análise de dados - bolsa bia (UFC)

Este repositório foi criado para organizar e registrar o progresso das análises de dados desenvolvidas durante minha **Bolsa de Iniciação Acadêmica (BIA)** no projeto de **Formação de apicultores cearenses com ferramentas tecnológicas desenvolvidas para da apicultura e precisão no semiárido** na Universidade Federal do Ceará.

## 🐝 Sobre o projeto
O trabalho consiste no suporte técnico à pesquisa de mestrado realizada no apiário da ufc, sob orientação do **prof. Rafael Braga**. a pesquisa foca no monitoramento de ninhos de abelhas para entender como o microclima interno (temperatura e umidade) é mantido pelas larvas e pela estrutura do ninho.

## 🎯 Objetivo do repositório
Este espaço servirá para:
* Documentar o tratamento dos dados brutos coletados pelos sensores.
* Registrar a evolução dos scripts de análise.
* Centralizar as visualizações e métricas geradas para discussão com a equipe de pesquisa.

## 🚀 Como executar o projeto

### 1. Dependências
Para rodar os scripts, você precisará do Python instalado e das seguintes bibliotecas:
* **Pandas**: Para manipulação e tratamento dos dados.
* **Matplotlib**: Para geração dos gráficos.

Você pode instalar as duas de uma vez com o comando:
```bash
pip install pandas matplotlib
```

### 2. Execução
Com as dependências instaladas, você pode executar os scripts através do terminal:

Para gerar as métricas estatísticas:
```bash
python scripts/metricasDados.py
```

Para gerar os gráficos dos sensores:
```bash
python scripts/graficosDados.py
```