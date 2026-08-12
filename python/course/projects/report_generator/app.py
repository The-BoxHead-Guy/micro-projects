import streamlit as st
from data import calculate_summaries, read_sellings
from reports import generar_pdf

st.set_page_config(page_title="Reportes de ventas")
st.title("Generador de reportes de ventas")
st.write("Sube tu CVS de ventas y descarga el reporte PDF.")

file = st.file_uploader("Archivo CSV", type="csv")

if file is not None:
    df = read_sellings(file)
    summaries = calculate_summaries(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Ventas", summaries.get("num_ventas"))
    col2.metric("Ingresos", f"${summaries.get('total_ingresos'):.2f}")
    col3.metric("Precio promedio", f"${summaries.get('precio_promedio'):.2f}")

    st.subheader("Detalle de ventas")
    st.dataframe(df, width="stretch")

    pdf_bytes = generar_pdf(df, summaries)

    if type(pdf_bytes) is bytes:
        st.download_button(
            "Descargar reporte PDF",
            data=pdf_bytes,
            file_name="reporte_ventas.pdf",
            mime="application/pdf",
        )
else:
    st.info("Esperando un archivo CSV...")
