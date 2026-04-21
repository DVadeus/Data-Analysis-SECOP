import pandas as pd

def to_dataframe(data):
    df = pd.DataFrame(data)

    # Transformación de fechas

    if "fecha_de_inicio_del_contrato" in df.columns:
        df["fecha_de_inicio_del_contrato"] = pd.to_datetime(df["fecha_de_inicio_del_contrato"], errors = "coerce")

    if "fecha_de_firma" in df.columns:
        df["fecha_de_firma"] = pd.to_datetime(df["fecha_de_firma"], errors="coerce")

    if "fecha_de_fin_del_contrato" in df.columns:
        df["fecha_de_fin_del_contrato"] = pd.to_datetime(df["fecha_de_fin_del_contrato"], errors="coerce")
    
    if "ultima_actualizacion" in df.columns:
        df["ultima_actualizacion"] = pd.to_datetime(df["ultima_actualizacion"], errors="coerce")

    if "fecha_de_notificaci_n_de_prorrogaci_n" in df.columns:
        df["fecha_de_notificaci_n_de_prorrogaci_n"] = pd.to_datetime(df["fecha_de_notificaci_n_de_prorrogaci_n"], errors="coerce")
    
    if "fecha_inicio_liquidacion" in df.columns:
        df["fecha_inicio_liquidacion"] = pd.to_datetime(df["fecha_inicio_liquidacion"], errors="coerce")
    
    if "fecha_fin_liquidacion" in df.columns:
        df["fecha_fin_liquidacion"] = pd.to_datetime(df["fecha_fin_liquidacion"], errors="coerce")
    
    # Transformación de columnas categóricas

    if "departamento" in df.columns:
        df["departamento"] = df["departamento"].astype('category')
    
    if "ciudad" in df.columns:
        df["ciudad"] = df["ciudad"].astype('category')

    if "localizaci_n" in df.columns:
        df["localizaci_n"] = df["localizaci_n"].astype('category')

    if "orden" in df.columns:
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


    # Columnas booleanas
    df["es_grupo"] = df["es_grupo"].map({'Si': True, 'No': False})
    df["es_pyme"] = df["es_pyme"].map({'Si': True, 'No': False})
    df["liquidaci_n"] = df["liquidaci_n"].map({'Si': True, 'No': False})
    df["obligaci_n_ambiental"] = df["obligaci_n_ambiental"].map({'Si': True, 'No': False})
    df["obligaciones_postconsumo"] = df["obligaciones_postconsumo"].map({'Si': True, 'No': False})
    df["reversion"] = df["reversion"].map({'Si': True, 'No': False})
    df["espostconflicto"] = df["espostconflicto"].map({'Si': True, 'No': False})
    df["el_contrato_puede_ser_prorrogado"] = df["el_contrato_puede_ser_prorrogado"].map({'Si': True, 'No': False})
    df["tipo_de_documento_ordenador_del_gasto"] = df["tipo_de_documento_ordenador_del_gasto"].map({'Si': True, 'No': False})
    df["tipo_de_documento_supervisor"] = df["tipo_de_documento_supervisor"].map({'Si': True, 'No': False})
    df["documentos_tipo"] = df["documentos_tipo"].map({'Si': True, 'No': False})

    return df