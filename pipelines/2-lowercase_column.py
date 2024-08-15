def lowercas_columns(data):
    data.columns = data.columns.str.lower()
    return data