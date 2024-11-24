import os
import json
import pandas as pd

# Caminho para o diretório com os arquivos JSON
diretorio = "/home/paulo/Ondedrive/PythonPaulo/Bolsa/Resultados"

# Lista para armazenar os dados carregados
dados_completos = []

# Iterar pelos arquivos no diretório
for arquivo in os.listdir(diretorio):
	if arquivo.endswith(".json"):
		nome_arquivo = os.path.splitext(arquivo)[0]
		caminho_arquivo = os.path.join(diretorio, arquivo)
		with open(caminho_arquivo, 'r', encoding='utf-8') as f:
			dados = json.load(f)
			# Adicionar o nome do arquivo como uma coluna em cada registro
			for registro in dados:
				registro['nome_arquivo'] = nome_arquivo
			dados_completos.extend(dados)

# Converter para um DataFrame do pandas
# Supondo que os dados sejam do tipo lista de dicionários
df = pd.DataFrame(dados_completos)

# Exibir os primeiros registros
print(df.head())

# Salvar em um novo arquivo consolidado no formato Excel
caminho_saida = "/home/paulo/Ondedrive/PythonPaulo/Bolsa/Resultados/consolidado.xlsx"
df.to_excel(caminho_saida, index=False, sheet_name='Consolidado')

print(f"Arquivo consolidado salvo em: {caminho_saida}")