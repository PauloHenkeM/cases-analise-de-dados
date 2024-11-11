
# Objetivo
Desenvolver uma análise financeira deve identificar pagamentos e recebimentos duplicados, verificando discrepâncias nas transações. Além disso, ela deve possibilitar a visualização clara do fluxo de caixa, destacando entradas e saídas para facilitar o controle financeiro e a tomada de decisões. 

# Informações
- **Linguagem de Programação**: Python  
- **Versão**: 3.11.2  
- **Ambiente:** CT no Proxmox
- **Sistema Operacional**: Debian 12

# Links
- [BD](https://raw.githubusercontent.com/PauloHenkeM/cases-analise-de-dados/refs/heads/main/Exemplo.LTDA/BD.csv)
- Dashboard
- [Análise](https://github.com/PauloHenkeM/cases-analise-de-dados/blob/main/Exemplo.LTDA/Analise.md)

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