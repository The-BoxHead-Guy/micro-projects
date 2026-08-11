import pandas as pd


def read_sellings(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df["Precio"] = df["Precio"].str.replace("$", "", regex=False)
    df["Precio"] = df["Precio"].astype(float)

    return df


def calculate_summaries(df: pd.DataFrame) -> dict:
    total_amount = (df["Precio"] * df["Cantidad"]).sum()
    overall_price = df["Precio"].mean()
    maximum_selling = df["Precio"].max()
    minimun_selling = df["Precio"].min()
    length_selling = len(df)

    return {
        "total_ingresos": total_amount,
        "precio_promedio": overall_price,
        "venta_mayor": maximum_selling,
        "venta_menor": minimun_selling,
        "num_ventas": length_selling,
    }
