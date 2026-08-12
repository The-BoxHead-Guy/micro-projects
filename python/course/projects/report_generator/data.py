from typing import TypedDict

import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile


class Summary(TypedDict):
    total_ingresos: float
    precio_promedio: float
    venta_mayor: float
    venta_menor: float
    num_ventas: int


def read_sellings(file_path: str | UploadedFile) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df["Precio"] = df["Precio"].str.replace("$", "", regex=False)
    df["Precio"] = df["Precio"].astype(float)

    return df


def calculate_summaries(df: pd.DataFrame) -> Summary:
    total_amount = (df["Precio"] * df["Cantidad"]).sum()
    overall_price = df["Precio"].mean()
    maximum_selling = df["Precio"].max()
    minimun_selling = df["Precio"].min()
    length_selling = len(df)

    summary: Summary = {
        "total_ingresos": total_amount,
        "precio_promedio": overall_price,
        "venta_mayor": maximum_selling,
        "venta_menor": minimun_selling,
        "num_ventas": length_selling,
    }

    return summary
