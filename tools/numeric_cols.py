def numeric_cols(df, columns, dicionario={}):
    for column in columns:
        for chave, valor in enumerate(df[column].unique()):
            dicionario[valor] = chave

        df[f'n_{column}'] = t_train[column].map(dicionario)
        
    return df