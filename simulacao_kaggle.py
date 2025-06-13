import pandas as pd
import matplotlib.pyplot as plt
import time

# Le o csv
data = pd.read_csv('dados_simulador_kaggle.csv')

# Converte a coluna para datetime
if 'Data' in data.columns:
    data['Data'] = pd.to_datetime(data['Data'])
else:
    # Se não, é criada uma coluna de data e hora simulada
    data['Data'] = pd.date_range(start='2025-06-12 00:00:00', periods=len(data), freq='2S')

# Simula a leitura dos sensores
for index, row in data.iterrows():
    temperatura = row['Temperatura']
    umidade = row['Umidade']
    print(f"Dados do Sensor Simulado - Temperatura: {temperatura}C, Umidade: {umidade}%")

# Gera o gráfico
plt.figure(figsize=(10, 5))
plt.plot(data['Data'], data['Temperatura'], label='Temperatura (C)', color='red', marker='o')
plt.plot(data['Data'], data['Umidade'], label='Umidade (%)', color='blue', marker='x')

# Configurações do gráfico
plt.xlabel('Data e Hora')
plt.ylabel('Leitura')
plt.title('Simulação de Leitura de Temperatura e Umidade')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Cria a pasta Imagens se não existir
import os
os.makedirs("Imagens", exist_ok=True)

# Salva a imagem do gráfico em png
plt.savefig('Imagens/grafico_temperatura_umidade_kaggle.png')

# Exibe o gráfico
plt.show()
