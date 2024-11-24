from base64 import b64decode, b64encode
import requests
import json

# Input para a quantidade de páginas
quantidade_paginas = int(input("Quantidade de páginas: "))

# Input das URLs
urls = [input(f"URL completa da página {i + 1}: ") for i in range(quantidade_paginas)]

# Lista para armazenar todos os resultados
resultados = []
trading_name = ""

print("\nColetando dados...\n")

try:
	for i, url in enumerate(urls):
		# Extrai e decodifica a string Base64 da URL
		base64_string = url.split('/')[-1]
		dados = b64decode(base64_string).decode()
		dados_dict = json.loads(dados)
		
		# Obtém o tradingName na primeira iteração
		if i == 0 and "tradingName" in dados_dict:
			trading_name = dados_dict["tradingName"]
		
		# Atualiza a página no dicionário
		dados_dict["pageNumber"] = i + 1
		
		# Re-encode em Base64 e atualiza a URL
		nova_base64_string = b64encode(json.dumps(dados_dict).encode()).decode()
		nova_url = url.rsplit('/', 1)[0] + '/' + nova_base64_string
		
		# Faz a requisição
		r = requests.get(nova_url)
		resposta = r.json()
		
		# Adiciona os resultados coletados
		if "results" in resposta and resposta["results"]:
			resultados.extend(resposta["results"])
			print(f"Dados da página {i + 1} coletados com sucesso.")
		else:
			print(f"Página {i + 1} sem resultados ou inválida.")

except Exception as e:
	print("Erro durante a coleta:", e)

# Verifica se tradingName foi encontrado
if not trading_name:
	trading_name = "Desconhecido"

# Caminho para salvar o arquivo JSON
caminho_arquivo = f"/home/paulo/Ondedrive/PythonPaulo/Bolsa/Proventos-{trading_name}.json"

# Salva os resultados no arquivo
try:
	with open(caminho_arquivo, "w") as arquivo:
		json.dump(resultados, arquivo, indent=2, ensure_ascii=False)
	print(f"\nResultados salvos com sucesso em: {caminho_arquivo}")
except Exception as e:
	print(f"Erro ao salvar o arquivo JSON: {e}")