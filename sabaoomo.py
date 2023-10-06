# @title 1. Importa as bibliotecas necessárias para a Análise Exploratória de Dados (AED)

import io
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statistics

# @title 2. Importa o arquivo omo.csv para o dataframe df_omo

from google.colab import files
uploaded = files.upload()
df_omo = pd.read_csv('omo.csv', sep=',', encoding='utf-8')

# @title 3. Visualiza o arquivo omo.csv importado

df_omo

# @title 4. Gera estatísticas de tendência central para o campo PESO

# Calcula as medidas de tendência central

contagem = df_omo['PESO'].count()
media = df_omo['PESO'].mean()
moda = statistics.mode(df_omo['PESO'])
minimo = df_omo['PESO'].min()
Q1 = df_omo['PESO'].quantile(0.25)
mediana = df_omo['PESO'].median()
Q3 = df_omo['PESO'].quantile(0.75)
maximo = df_omo['PESO'].max()
AIQ = Q3 - Q1
outlier_sup = Q3 + (1.5 * AIQ)
outlier_inf = Q1 - (1.5 * AIQ)

# Exibe os resultados

peso_esperado_max = 1000 * 1.03
peso_esperado_min = 1000 * 0.97

print(f"Peso Esperado Máximo: {peso_esperado_max:.2f}")
print(f"Peso Esperado Mínimo: {peso_esperado_min:.2f}")
print(f"Contagem: {contagem:.2f}")
print(f"Média: {media:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Mínimo: {minimo:.2f}")
print(f"Q1: {Q1:.2f}")
print(f"Mediana = Q2: {mediana:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"Máximo: {maximo:.2f}")
print(f"Amplitude Interquartil (AIQ): {AIQ:.2f}")
print(f"Outliers Inferiores: {outlier_inf:.2f}")
print(f"Outliers Superiores: {outlier_sup:.2f}")
print(' ')

# Análises específicas

if media == mediana:
  print('A distribuição de dados é simétrica.')
elif media < mediana:
    print('A distribuição de dados é assimétrica com valores menores à esquerda.')
elif media < mediana:
    print('A distribuição de dados é assimétrica com valores menores à esquerda.') 

# @title 5. Desenha o boxplot utilizando a biblioteca Seaborn

sns.set_palette("pastel") #Define a paleta de cores pastel. Veja mais em: https://www.codecademy.com/article/seaborn-design-i e https://www.codecademy.com/article/seaborn-design-ii
sns.boxplot(x=df_omo['PESO'], color='orange', width=0.2)
plt.xticks(np.arange(900, 1100, 20)) # Define o intervalo de 900 a 1100 com passo 20 no eixo x
plt.title('Peso das Embalagens de OMO')
plt.xlabel('Peso (gramas)')
plt.show()

# @title 5. Gera estatísticas de dispersão para o campo PESO

# Calcular a variância
variancia = df_omo['PESO'].var()

# Calcular o desvio padrão
desvio_padrao = df_omo['PESO'].std()

# Calcular CV%
cvp = (desvio_padrao/ media)*100

# Calcular o percentual da amostra que está entre -1 dp e + 1dp,
# -2 dp e + 2dp e -3 dp e + 3dp. # Para uma curva normal 
# (grande repetibilidade) é esperado que # 66,67% da amostra esteja 
# entre -2 dp e + 2dp, 95% entre -2dp e +2dp e 99,7% entre -3dp e +3dp.

um_dp = desvio_padrao
dois_dp = (2 * desvio_padrao)
tres_dp = (3 * desvio_padrao)

valores_entre_1dp = df_omo[(df_omo['PESO'] >=(media-um_dp)) & (df_omo['PESO'] <= (media+um_dp))]
quantidade_valores_entre_1dp = len(valores_entre_1dp)
quantidade_valores_entre_1dp_percentual = (quantidade_valores_entre_1dp/contagem)*100

valores_entre_2dp = df_omo[(df_omo['PESO'] >=(media-dois_dp)) & (df_omo['PESO'] <= (media+dois_dp))]
quantidade_valores_entre_2dp = len(valores_entre_2dp)
quantidade_valores_entre_2dp_percentual = (quantidade_valores_entre_2dp/contagem)*100

valores_entre_3dp = df_omo[(df_omo['PESO'] >=(media-tres_dp)) & (df_omo['PESO'] <= (media+tres_dp))]
quantidade_valores_entre_3dp = len(valores_entre_3dp)
quantidade_valores_entre_3dp_percentual = (quantidade_valores_entre_3dp/contagem)*100

print(f'Variância: {variancia:.2f}')
print(f'Desvio Padrão: {desvio_padrao:.2f}')
print(f'CV%: {cvp:.2f} %')
print(f'Entre -1 e +1 desvios-padrão (esperado 66,67% entre {(media-um_dp):.2f}g e {(media+um_dp):.2f}g): {quantidade_valores_entre_1dp_percentual :.2f} %')
print(f'Entre -2 e +2 desvios-padrão (esperado 95% entre {(media-dois_dp):.2f}g e {(media+dois_dp):.2f}g): {quantidade_valores_entre_2dp_percentual :.2f} %')
print(f'Entre -2 e +2 desvios-padrão (esperado 99,7% entre {(media-tres_dp):.2f}g e {(media+tres_dp):.2f}g): {quantidade_valores_entre_3dp_percentual :.2f} %')

# @title 6. Plotar o histograma com curva de densidade
sns.histplot(df_omo['PESO'], kde=True, bins=15, color='blue')  # kde=True para incluir a curva de densidade
plt.title('Histograma do Peso das Embalagens de OMO')
plt.xlabel('Peso (gramas)')
plt.ylabel('Frequência')
plt.show()

7. CONCLUSÃO

As 1001 amostras de peso, medida em gramas, de caixas de sabão em pó OMO, cujo peso nominal é 1kg mostram que:

. 25% das caixas tem peso menor que 964 gramas (Q1). Só por essa medida sabemos que as caixas estão NÃO CONFORMES, pois a totalidade da amostra deveria estar entre 970g e 1030g.

. 50% das caixas tem peso menor que 1001 gramas (mediana = Q2)

. 75% das caixas tem peso menor que 1037 gramas (Q3). Essa informação mostra que 25% das caixas entre Q2 e Q3 tem uma variação de peso entre 1001g (Q2) e 1037g (Q3).

. O coeficiente de variação percentual, baseado na divisão do desvio padrão pela média indica uma variação de 4,12%, acima do máximo permitido de 3%.
