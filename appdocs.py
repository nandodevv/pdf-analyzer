from openai import OpenAI  #→ importas solo la clase OpenAI de dentro de la librería

import streamlit as st
import PyPDF2   #→ importas toda la libreria 

from dotenv import load_dotenv #dotenv es una libreria , 
#su unica funcion es leer el archivo env y leer las claves que hay dentro
import os #os es una libreria que viene con python y te permite acceder a cosas
#del sistema operativo: como las variables de entorno



load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#Exacto. client es tu conexión a GPT. Es una variable que llama a GPT
# Cada vez que quieras preguntarle algo lo harás a través de client.




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
    
    if pregunta:
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente que responde preguntas sobre documentos."},
                {"role": "user", "content": f"Documento: {texto}\n\nPregunta: {pregunta}"}
            ]
        )
        st.write(respuesta.choices[0].message.content)



            #1. if pregunta= Si existe una pregunta del usuario. pregunta =input del usuario
            # 2. respuesta(variable) = llamamos a gpt con client y 
            # la funcion chat completions.create 
            # 2.1 Especificamos el modelo
            #. 2.2 Messages (lista de dos mensajes) asi es como gpt entiende una
            #conversacion: 2 roles
            # a) system, content: Le dices como debe comprotarse (instrucciones)
            # b) user , content : es el input del usuario que le das tu a la ia
            #junto con el texto para que responda 

        

     


