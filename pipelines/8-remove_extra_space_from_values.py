def remove_extra_space_from_values(data):
    for feature in data.select_dtypes(include = 'O').columns:
        data[feature] = data[feature].apply(lambda value: np.nan if pd.isnull(value) else value.replace(' ', ''))
    return data