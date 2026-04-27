def get_new_records(df_new, df_existing):

    existing_ids = set(df_existing["contract_id"])

    df_filtered = df_new[~df_new["contract_id"].isin(existing_ids)]

    return df_filtered