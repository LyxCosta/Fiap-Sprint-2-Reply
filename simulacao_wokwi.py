import pandas as pd
import matplotlib.pyplot as plt
import re

# Le o csv
with open('dados_sensor_wokwi.csv', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Inicia as listas
sensores = []
temperaturas = []
umidades = []

sensor_atual = None

# Processa linha por linha
for linha in linhas:
    linha = linha.strip()

    if linha.startswith("Sensor"):
        sensor_atual = linha.strip()
    elif "Temperatura" in linha and "Umidade" in linha:
        match = re.search(r'Temperatura (\d+,\d+|\d+\.\d+)\s*C\s+Umidade (\d+,\d+|\d+\.\d+)\s*%', linha)
        if match and sensor_atual:
            temp = match.group(1).replace(',', '.')
            umi = match.group(2).replace(',', '.')
            sensores.append(sensor_atual)
            temperaturas.append(float(temp))
            umidades.append(float(umi))

# Cria uma sequencia de tempo simulada
datas = pd.date_range(start='2025-06-12 00:00:00', periods=len(sensores), freq='2S')

# Cria um DataFrame
df = pd.DataFrame({
    'Data': datas,
    'Sensor': sensores,
    'Temperatura': temperaturas,
    'Umidade': umidades
}).reset_index(drop=True)

# Separa os sensores
sensor1 = df[df['Sensor'] == 'Sensor 1']
sensor2 = df[df['Sensor'] == 'Sensor 2']

# Exibe os dados
print("\n--- Leituras do Sensor 1 ---")
for _, row in sensor1.iterrows():
    print(f"{row['Sensor']} - Temperatura: {row['Temperatura']}C, Umidade: {row['Umidade']}%")

print("\n--- Leituras do Sensor 2 ---")
for _, row in sensor2.iterrows():
    print(f"{row['Sensor']} - Temperatura: {row['Temperatura']}C, Umidade: {row['Umidade']}%")

# Gera os gráficos
fig, axs = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

# Gráfico de Temperatura
axs[0].plot(sensor1['Data'], sensor1['Temperatura'], label='Sensor 1 - Temperatura', color='red', marker='o')
axs[0].plot(sensor2['Data'], sensor2['Temperatura'], label='Sensor 2 - Temperatura', color='orange', marker='x')
axs[0].set_ylabel('Temperatura (°C)')
axs[0].legend()
axs[0].grid(True)

# Gráfico de Umidade
axs[1].plot(sensor1['Data'], sensor1['Umidade'], label='Sensor 1 - Umidade', color='blue', marker='o')
axs[1].plot(sensor2['Data'], sensor2['Umidade'], label='Sensor 2 - Umidade', color='cyan', marker='x')
axs[1].set_ylabel('Umidade (%)')
axs[1].set_xlabel('Data e Hora')
axs[1].legend()
axs[1].grid(True)

# Ajustes finais
fig.suptitle('Leituras dos Sensores Wokwi - Temperatura e Umidade', fontsize=14)
fig.autofmt_xdate(rotation=45)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # garante espaço pro título

# Cria a pasta Imagens se não existir
import os
os.makedirs("Imagens", exist_ok=True)

# Correção para evitar problemas caso o titulo não seja exibido corretamente
plt.savefig("Imagens/grafico_temperatura_umidade_wokwi.png", bbox_inches='tight')

# Mostra o gráfico
plt.show()
