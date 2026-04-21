import os
import uuid


def save_parquet(df, base_path):
    os.makedirs(os.path.dirname(base_path), exist_ok=True)
    file_name = f"data_part_{uuid.uuid4().hex}.parquet"
    full_path = os.path.join(base_path, file_name)
    print(f"Guardando en archivo: {full_path}")
    df.to_parquet(full_path, index = False)