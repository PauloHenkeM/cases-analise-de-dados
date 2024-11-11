
# Objetivo
Desenvolver uma análise financeira que permita identificar pagamentos e recebimentos duplicados, bem como possibilitar a visualização do fluxo de caixa.

# Informações
- **Linguagem de Programação**: Python  
- **Versão**: 3.11.2  
- **Sistema Operacional**: Debian 12

# Código Python para Geração da Base de Dados
```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurações gerais
n = 10000  # Número de registros
categorias = ["Venda", "Serviço", "Salário", "Imposto", "Outros"]
tipos_movimento = ["Entrada", "Saída"]

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

# Observações variadas
observacoes = [
    "Pagamento por venda", "Recebimento de cliente X", "Despesa de operação",
    "Pagamento de imposto", "Reembolso de serviço", "Salário", "Outros recebimentos"
]
observacao = np.random.choice(observacoes, n)

# Criação do DataFrame
df = pd.DataFrame({
    "ID_Movimento": id_movimento,
    "Data": datas,
    "Tipo_Movimento": tipo_movimento,
    "Categoria": categoria,
    "Valor": valor,
    "Observacao": observacao
})

# Exporta para CSV
output_path = "/home/paulo/caminho/BD.csv"
df.to_csv(output_path, index=False, sep=";", encoding="utf-8-sig")

output_path
```