from openai import OpenAI  

import streamlit as st
import PyPDF2   
from dotenv import load_dotenv  
import os 




load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




st.title("Analizador de documentos")
st.write("Sube un documento y hazle preguntas")
archivo =st.file_uploader("Sube tu archivo aqui", type="pdf")


if archivo is not None:
    st.write("Archivo subido correctamente")
    pregunta = st.text_input("Haz una pregunta sobre el documento")
    lector = PyPDF2.PdfReader(archivo)
    texto = ""
    for pagina in lector.pages:
        texto += pagina.extract_text()
    st.write(texto)
    if pregunta:
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente que responde preguntas sobre documentos."},
                {"role": "user", "content": f"Documento: {texto}\n\nPregunta: {pregunta}"}
            ]
        )
        st.write(respuesta.choices[0].message.content)



         

        

     


