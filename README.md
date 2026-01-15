# 📊 ABI Dashboard — Business & Data Quality Analysis

Dashboard interativo para **análise de dados de vendas**, **qualidade do dataset** e **avaliação da saúde do negócio**, desenvolvido com **Python e Streamlit**.

O objetivo do projeto é transformar arquivos CSV em **insights executivos**, combinando métricas de negócio, análise temporal, score de qualidade e geração de relatórios profissionais.

---

https://github.com/user-attachments/assets/752e73bd-24e1-4274-b177-559c867ac32b

---


## 🚀 Funcionalidades

### 📌 Visão Geral do Dataset
- Número de linhas e colunas
- Tipos de dados
- Colunas numéricas e categóricas
- Valores nulos por coluna
- Percentual total de dados faltantes

### 📈 KPIs Principais
- Receita total
- Preço médio
- Produto mais vendido
- Cliente mais recorrente
- Quantidade total vendida

### 📊 Análise Temporal
- Comparação automática entre os dois últimos meses
- Cálculo de variação percentual da receita
- Identificação de crescimento ou queda

### 🧠 Business Score
Score de 0 a 100 baseado em:
- Percentual de dados faltantes
- Presença de outliers
- Concentração excessiva de receita
- Diversidade de clientes

### 📄 Relatórios
- Exportação do relatório executivo em **JSON**
- Geração de **Relatório Executivo em PDF**
- Conteúdo pronto para tomada de decisão

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas**
- **Streamlit**
- **Matplotlib**
- **ReportLab**

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```
git clone https://github.com/seu-usuario/abi-dashboard.git
cd abi-dashboard
```

### 2️⃣ Criar e ativar a virtualenv
```
python -m venv .venv
```

- Windows
```
.venv\Scripts\activate
```

- Linux / macOS
```
source .venv/bin/activate
```

### 3️⃣ Instalar as dependências
```
pip install -r requirements.txt
```

### 4️⃣ Executar o app
```
streamlit run src/app.py
```

### 📁 Dataset Esperado
O arquivo CSV deve conter, no mínimo, as seguintes colunas:

date, product, customer, quantity, price, revenue


Caso a coluna revenue não exista, ela pode ser calculada como:
quantity * price

### 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em:

- Portfólio profissional
- Análise de dados aplicada ao negócio
- Automação de insights
- Entrega de valor executivo

### 👨‍💻 Autor

Lucas Gomes
Back-End Developer | Automação & Análise de Dados

Python • SQL • Streamlit • AWS

🔗 LinkedIn: https://www.linkedin.com/in/lucasdsgomes/
