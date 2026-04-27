from src.config import START_YEAR, END_YEAR, OUTPUT_PATH
from src.extract import fetch_data
from services.parquet_service import save_parquet
from src.transform import to_dataframe
from src.state import save_state, load_state
from datetime import datetime, timedelta

def run_first_pipeline():

    #Datos por año
    for year in range(START_YEAR, END_YEAR):
        print(f"Procesando {year}...")

        where = f"""
        fecha_de_inicio_del_contrato >= '{year}-01-01T00:00:00.000'
        AND fecha_de_inicio_del_contrato < '{year + 1}-01-01T00:00:00.000'
        """

        data = fetch_data(where_clause=where)
        df = to_dataframe(data)

        if not df.empty:
            path = f"{OUTPUT_PATH}/year={year}/data.parquet"
            save_parquet(df, base_path=path)

        #Datos nulos
    print(f"Procesando NULLs...")

    data_null = fetch_data(where_clause="fecha_de_inicio_del_contrato IS NULL")
    df_null = to_dataframe(data_null)

    if not df_null.empty:
        path = f"{OUTPUT_PATH}/nulls/data.parquet"
        save_parquet(df_null, path)

LOOKBACK_DAYS = 0

def run_incremental():

    state = load_state()
    last_fecha = datetime.fromisoformat(state["fecha_de_inicio_del_contrato"])

    # Ventana de seguridad
    start_date = last_fecha - timedelta(days=LOOKBACK_DAYS)

    where = f"""
    fecha_de_inicio_del_contrato >= '{start_date.isoformat()}'
    """

    print(f"Extrayendo desde {start_date}")

    data = fetch_data(where)
    df = to_dataframe(data)

    if df.empty:
        print("No hay datos nuevos")
        return
    
    df = df.drop_duplicates(subset=["id_contrato"])

    # Partición por año

    df["year"] = df["fecha_de_inicio_del_contrato"].dt.year

    for year, df_year in df.groupby("year"):
        path = f"{OUTPUT_PATH}/year={year}/"
        save_parquet(df_year, path)

    # Actualizar estado
    new_max_date = df["fecha_de_inicio_del_contrato"].max()

    state["fecha_de_inicio_del_contrato"] = new_max_date.isoformat()
    save_state(state)

    print(f"Nuevo estado: {new_max_date}")



if __name__ == "__main__":
    #run_first_pipeline()
    run_incremental()
