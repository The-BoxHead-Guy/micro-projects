from data import calculate_summaries, read_sellings
from reports import generar_pdf


def main():
    df = read_sellings("ventas.csv")
    summaries = calculate_summaries(df)

    print(f"Ventas leidas: {summaries['num_ventas']}")
    print(f"Ingresos totales: {summaries['total_ingresos']:.2f}")

    generar_pdf(df, summaries, "reporte_ventas.pdf")
    print("Listo, PDF generado")


if __name__ == "__main__":
    main()
