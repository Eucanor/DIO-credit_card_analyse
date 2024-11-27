import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title ("Upload de arquivo DIO - Desafio 2 - Azure _Fake Docs")
    upload_file = st.file_uploader("Escolha um arquivo", type=[png, jpg,jpeg])

    if upload_file is not None:
        filename = upload_file.name
        # Enviar para blob storage
        blob_url = ""
        if blob_url:
            st.write("Arquivo {filename} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write("Erro ao enviar o arquivo {filename} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.write("<h1 style='color: green;'>Cartão válido</h1>", unsafe_allow_html=True)
        st.write("Nome do titular:  {credit_card_info['card_name']}")
        st.write("Banco Emissor:  {credit_card_info['bank_name']}")
        st.write("Data de Validade:  {credit_card_info['expiry_date']}")
    else:
        st.write("<h1 style='color: red;'>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__  == "__main":
    configure_interface()
