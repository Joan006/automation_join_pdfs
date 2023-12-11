"""
Description: App para unir pdfs en uno solo 
@utor = JoanMtz
"""
import streamlit as st
import PyPDF2

# <--- Variables --->
output_pdf = "documents/pdf_final.pdf"

# <-- FUNCIONES -->
def unir_pdf(output_path, documents):
  # se crea un objeto PdfMerger para combinar los archivos PDF
  pdf_final=PyPDF2.PdfMerger()

  for document in documents:
    pdf_final.append(document)  # Agregar cada PDF a la fusion
  
  pdf_final.write(output_path)  # Guarda el PDF combinado en la ruta de salida

# <--- FRONT --->

st.image("assets/imagen_pdf.jpeg")
st.header("Unir PDF")
st.subheader("Adjuntar PDFs para unir")

pdf_adjuntos = st.file_uploader(label="", accept_multiple_files=True)

unir = st.button(label="Unir PDFs", )  # Se crea un boton


# <-- Funcion para unir -->

if unir:

  if len(pdf_adjuntos) <= 1:
    st.warning("Debes adjuntar mas de un PDF")
  else:
    
    unir_pdf(output_pdf, pdf_adjuntos)
    st.success("Desde aqui puedes descargar el PDF finalizado")
    with open(output_pdf, "rb") as file: 
      pdf_data = file.read()
    st.download_button(label="Descarga PDF final", data=pdf_data, file_name="pdf_final.pdf")

