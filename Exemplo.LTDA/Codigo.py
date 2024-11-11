import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurações gerais
n = 10000  # Número de registros
categorias = ["Venda", "Serviço", "Salário", "Imposto", "Outros"]
tipos_movimento = ["Entrada", "Saída"]
clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]

# Geração dos dados
np.random.seed(0)

# Gera ID da movimentação com duplicidades
id_movimento = np.random.randint(1000, 5000, n)

# Datas nos últimos 2 anos
data_inicial = datetime.now() - timedelta(days=2*365)
datas = [data_inicial + timedelta(days=np.random.randint(0, 730)) for _ in range(n)]

# Tipo de movimento (Entrada ou Saída)
tipo_movimento = np.random.choice(tipos_movimento, n)

# Categoria da movimentação
categoria = np.random.choice(categorias, n)

# Valor da transação, entre 10 e 50000
valor = np.round(np.random.uniform(10, 50000, n), 2)

# Cliente aleatório
cliente = np.random.choice(clientes, n)

# Criação do DataFrame principal (sem a coluna 'Observacao')
df_movimentacoes = pd.DataFrame({
    "ID_Movimento": id_movimento,
    "Data": datas,
    "Tipo_Movimento": tipo_movimento,
    "Categoria": categoria,
    "Valor": valor,
    "Cliente": cliente
})

# DataFrame do plano de contas
df_plano_contas = pd.DataFrame({
    "id": [11, 12, 21, 22, 31, 32, 33],
    "movimento": ["Entrada", "Entrada", "Saída", "Saída", "Saída", "Saída", "Saída"],
    "lancamento": ["Receita", "Receita", "Custo", "Custo", "Despesa", "Despesa", "Despesa"],
    "conta": ["Operacional", "Não Operacional", "Operacional", "Operacional", 
              "Operacional", "Operacional", "Não Operacional"],
    "tipo": ["Receita", "Receita", "Fixo", "Variável", "Fixo", "Variável", "Fixo"]
})

# Caminhos de saída para os CSVs
output_path_movimentacoes = "/home/paulo/caminho/movimentacoes_financeiras.csv"
output_path_plano_contas = "/home/paulo/caminho/plano_de_contas.csv"

# Exporta os dados para CSVs separados
df_movimentacoes.to_csv(output_path_movimentacoes, index=False, sep=";", encoding="utf-8-sig")
df_plano_contas.to_csv(output_path_plano_contas, index=False, sep=";", encoding="utf-8-sig")
