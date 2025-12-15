# 🔮 Telco Churn Prediction: Retenção de Clientes com Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Sklearn-Model-orange)

Este projeto é uma solução completa de Ciência de Dados para prever a rotatividade de clientes (Churn) em uma empresa de telecomunicações. O objetivo é identificar clientes com alto risco de cancelamento para que a equipe de marketing possa agir preventivamente com campanhas de retenção.

## 🧠 O Problema de Negócio

A aquisição de novos clientes custa de 5 a 25 vezes mais do que manter os existentes. O desafio deste projeto foi:
1.  Criar um modelo preditivo capaz de identificar potenciais cancelamentos.
2.  Entender **quais fatores** levam o cliente a sair.
3.  Disponibilizar essa inteligência em uma interface simples para uso da equipe de negócios.

## 📊 Solução e Metodologia

O projeto seguiu o ciclo completo de Data Science:
* **ETL & Limpeza:** Tratamento de dados nulos, conversão de tipos e *feature engineering*.
* **Análise Exploratória (EDA):** Descoberta de padrões de comportamento.
* **Modelagem:** Treinamento de algoritmos (focando em *Random Forest*).
* **Otimização:** Ajuste de *Threshold* (limiar de decisão) para priorizar a detecção de churn (Recall).
* **Deploy:** Criação de um Web App interativo com Streamlit.

## 📈 Principais Insights e Resultados

O modelo final (Random Forest) foi otimizado para maximizar o **Recall** da classe de Churn (captura de ~62% dos cancelamentos), priorizando a identificação de riscos.

**Fatores Críticos descobertos:**
1.  **Tenure (Tempo de Casa):** Clientes novos (0-6 meses) têm risco altíssimo de sair. A fidelidade se consolida após 1 ano.
2.  **Mensalidade:** Clientes com tickets altos (acima de $70) cancelam com mais frequência do que clientes de planos básicos.
3.  **Tipo de Contrato:** Contratos mensais são os mais voláteis.

## 🛠️ Estrutura do Projeto

```bash
├── data/              # Conjuntos de dados (brutos e processados)
├── models/            # Modelos treinados (.pkl) e lista de features
├── notebooks/         # Jupyter Notebooks com a análise e experimentação
├── streamlit_app/     # Código da aplicação Web
│   └── app.py
├── requirements.txt   # Dependências do projeto
└── README.md
````


## 🚀 Como Executar o projeto
### 1. Clone o repositório


git clone [https://github.com/SEU-USUARIO/churn-prediction.git](https://github.com/SEU-USUARIO/churn-prediction.git)

cd churn-prediction
### 2. Instale as dependências
Recomenda-se usar um ambiente virtual (venv):

pip install -r requirements.txt
### 3. Execute o app
Para abrir a interface de previsão no seu navegador:
streamlit run streamlit_app/app.py

## 🧪 Exemplo de Uso do App
No painel lateral, insira os dados do cliente:
* Tenure: 2 meses
* Mensalidade: $90.00
* Contrato: Month-to-month

Resultado Esperado: O sistema exibirá um alerta de "Alto Risco de Churn" com a probabilidade calculada.
