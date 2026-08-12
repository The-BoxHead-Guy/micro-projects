from fpdf import FPDF, XPos, YPos


def generar_pdf(df, summaries, output_path=None) -> bytes | None:
    pdf = FPDF()
    pdf.add_page()

    # --- Cabecera con los colores del canal ---
    pdf.set_fill_color(10, 10, 10)  # negro
    pdf.set_text_color(166, 255, 0)  # verde lima
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(
        0,
        15,
        "REPORTE DE VENTAS",
        align="C",
        fill=True,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(8)

    # --- Bloque de resumenes ---
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Resumen general", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(
        0,
        7,
        f"Numero de ventas: {summaries['num_ventas']}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        7,
        f"Ingresos totales: ${summaries['total_ingresos']:.2f}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        7,
        f"Precio promedio: ${summaries['precio_promedio']:.2f}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        7,
        f"Venta mas alta: ${summaries['venta_mayor']:.2f}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        7,
        f"Venta mas baja: ${summaries['venta_menor']:.2f}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.ln(8)

    # --- Lista de ventas ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Detalle de ventas", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    pdf.set_font("Helvetica", "", 10)
    for indice, fila in df.iterrows():
        linea = f"- {fila['Vendedor']} vendio {fila['Cantidad']} x {fila['Producto']} a ${fila['Precio']:.2f}"
        pdf.cell(0, 6, linea, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # --- Guardar ---
    if output_path is None:
        print("No file path has been provided, returning bytes")
        return bytes(pdf.output())

    pdf.output(output_path)
