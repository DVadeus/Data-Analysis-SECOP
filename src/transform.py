import pandas as pd

def clean_columns(df):
    df.columns = df.columns.str.lower()
    return df

def to_dataframe(data):
    
    df = pd.DataFrame(data)

    if df.empty:
        return df
    
    df = clean_columns(df)

    # Transformación de fechas

    date_cols = [
        "fecha_de_inicio_del_contrato",
        "fecha_de_firma",
        "fecha_de_fin_del_contrato",
        "ultima_actualizacion",
        "fecha_de_notificaci_n_de_prorrogaci_n",
        "fecha_inicio_liquidacion",
        "fecha_fin_liquidacion"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors = "coerce")

    # Transformación de datos numéricos

    numeric_cols = [
        'valor_del_contrato',
        'valor_de_pago_adelantado',
        'valor_facturado',
        'valor_pendiente_de_pago',
        'valor_pagado',
        'valor_amortizado',
        'valor_pendiente_de',
        'valor_pendiente_de_ejecucion',
        'saldo_cdp',
        'saldo_vigencia',
        'presupuesto_general_de_la_nacion_pgn',
        'sistema_general_de_participaciones',
        'sistema_general_de_regal_as',
        'recursos_propios_alcald_as_gobernaciones_y_resguardos_ind_genas_',
        'recursos_de_credito',
        'recursos_propios'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = "coerce")

    # Transformación de Booleanos

    bool_map = {"Si": True, "No": False}

    bool_cols = [
        "es_grupo",
        "es_pyme",
        "liquidaci_n",
        "obligaci_n_ambiental",
        "obligaciones_postconsumo",
        "reversion",
        "espostconflicto",
        "el_contrato_puede_ser_prorrogado",
        "tipo_de_documento_ordenador_del_gasto",
        "tipo_de_documento_supervisor",
        "documentos_tipo"
    ]

    for col in bool_cols:
        if col in df.colums:
            df[col] = df[col].map(bool_map)

    # Transformación de columnas categóricas

    "departamento"
    "ciudad"
    "localizaci_n"
    "orden"

    

    if "departamento" in df.columns:
        df[] = df["departamento"].astype('category')
    
    if "ciudad" in df.columns:
        df[] = df["ciudad"].astype('category')

    if "localizaci_n" in df.columns:
        df[] = df["localizaci_n"].astype('category')

    if  in df.columns:
        df["orden"] = df["orden"].astype('category')

    if "sector" in df.columns:
        df["sector"] = df["sector"].astype('category')

    if "rama" in df.columns:
        df["rama"] = df["rama"].astype('category')

    if "entidad_centralizada" in df.columns:
        df["entidad_centralizada"] = df["entidad_centralizada"].astype('category')

    if "estado_contrato" in df.columns:
        df["estado_contrato"] = df["estado_contrato"].astype('category')

    if "tipo_de_contrato" in df.columns:
        df["tipo_de_contrato"] = df["tipo_de_contrato"].astype('category')

    if "modalidad_de_contratacion" in df.columns:
        df["modalidad_de_contratacion"] = df["modalidad_de_contratacion"].astype('category')

    if "justificacion_modalidad_de" in df.columns:
        df["justificacion_modalidad_de"] = df["justificacion_modalidad_de"].astype('category')

    if "condiciones_de_entrega" in df.columns:
        df["condiciones_de_entrega"] = df["condiciones_de_entrega"].astype('category')

    if "tipodocproveedor" in df.columns:
        df["tipodocproveedor"] = df["tipodocproveedor"].astype('category')

    if "origen_de_los_recursos" in df.columns:
        df["origen_de_los_recursos"] = df["origen_de_los_recursos"].astype('category')

    if "destino_gasto" in df.columns:
        df["destino_gasto"] = df["destino_gasto"].astype('category')

    if "puntos_del_acuerdo" in df.columns:
        df["puntos_del_acuerdo"] = df["puntos_del_acuerdo"].astype('category')

    if "pilares_del_acuerdo" in df.columns:
        df["pilares_del_acuerdo"] = df["pilares_del_acuerdo"].astype('category')

    if "nacionalidad_representante_legal" in df.columns:
        df["nacionalidad_representante_legal"] = df["nacionalidad_representante_legal"].astype('category')

    if "g_nero_representante_legal" in df.columns:
        df["g_nero_representante_legal"] = df["g_nero_representante_legal"].astype('category')

    if "tipo_de_cuenta" in df.columns:
        df["tipo_de_cuenta"] = df["tipo_de_cuenta"].astype('category')


    return df