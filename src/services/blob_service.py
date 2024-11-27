import os
import streamlit as st
from utils.Config import Config
from azure.storage.blob import BlobServiceClient

def upload_blob(file, file_name):
    try:
        blob_client = blob_service_client.get_blob_client(conteiner=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para a Azure Blob Storage")
        return None
    