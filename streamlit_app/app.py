import streamlit as st
import pandas as pd
import joblib
import os

# Configuração da página
st.set_page_config(page_title="Churn Prediction", page_icon="🔮", layout="wide")

@st.cache_resource
def load_model_and_features():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(current_dir,'..','models','random_forest_v1.pkl')
    features_path = os.path.join(current_dir,'..','models','features_names.pkl')

    try:
        model = joblib.load(model_path)
        features = joblib.load(features_path)
        return model, features
    except FileNotFoundError:
        st.error(f'Erro: Arquivos não encontrados.\nTentou buscar em {model_path}')
        return None, None
    
model, feature_names = load_model_and_features()
#INTERFACE

st.sidebar.header("Dados do Cliente")
st.sidebar.markdown("Preencha as informações abaixo:")

# --Coletando inputs
# Numéricos
tenure = st.sidebar.slider('Meses de Contrato (Tenure)', 0, 72, 12)
monthly_charges = st.sidebar.number_input('Mensalidade ($)', min_value=0, max_value=200, value=50)
total_charges = st.sidebar.number_input("Total Pago ($)", min_value=0.0, value=float(tenure * monthly_charges))

#Categoricos
internet_service = st.sidebar.selectbox("Serviço de Internet", ['DSL', 'Fiber optic', 'No'])
contract = st.sidebar.selectbox("Tipo de Contrato", ['Month-to-month', 'One year', 'Two year'])
payment_method = st.sidebar.selectbox("Método de Pagamento", [
    'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
])
online_security = st.sidebar.selectbox("Segurança Online", ['Yes', 'No', 'No internet service'])
tech_support = st.sidebar.selectbox("Suporte Técnico", ['Yes', 'No', 'No internet service'])
dependents = st.sidebar.selectbox("Possui Dependentes?", ['Yes', 'No'])
partner = st.sidebar.selectbox("Possui Parceiro(a)?", ['Yes', 'No'])
paperless = st.sidebar.selectbox("Fatura Digital (Paperless)?", ['Yes', 'No'])

#Processamento e Previsão
if st.button("Calcular Risco de Churn"):
    if model is not None:
        # Criar DataFrame com os dados brutos
        input_data = pd.DataFrame({
            'tenure': [tenure],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges],
            'InternetService': [internet_service],
            'Contract': [contract],
            'PaymentMethod': [payment_method],
            'OnlineSecurity': [online_security],
            'TechSupport': [tech_support],
            'Dependents': [dependents],
            'Partner': [partner],
            'PaperlessBilling': [paperless],
        })

    input_dummies = pd.get_dummies(input_data)
    input_final = input_dummies.reindex(columns=feature_names, fill_value=0)
    # Previsão
    probabilidade = model.predict_proba(input_final)[0][1]
    threshold = 0.40
    classe = 1 if probabilidade >= threshold else 0

    #exibição
    st.write('---')
    col1,col2 = st.columns(2)
    
    with col1:
        st.metric('Probabilidade de Churn',f'{probabilidade:.1%}')

    with col2:
        if classe == 1:
                
            st.error("🚨 ALERTA: Risco Alto de Cancelamento!")
            st.markdown(f"**Ação Recomendada:** Entrar em contato preventivo.")
        else:
            st.success("✅ Cliente Seguro")
            st.markdown("**Ação Recomendada:** Manter relacionamento padrão.")
                
else:
    st.info("Preencha os dados e clique em 'Calcular Risco'.")
