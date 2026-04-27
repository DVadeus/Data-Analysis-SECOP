import uuid
from io import BytesIO
from services.b2_service import get_b2_client

BUCKET_NAME="bucketSECOP"

def save_parquet(df, layer, partition_part):

    client = get_b2_client()

    file_name = f"part-{uuid.uuid4().hex}.parquet"

    key = f"{layer}/{partition_part}/{file_name}"

    # Almacenando el df en memoria
    buffer = BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    # Subiendo a B2
    client.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=buffer
    )

    print(f"Subido a B2: {key}")