def convert_missing_value(data):
    import numpy as np
    for column in data.columns:
        data[column] = data[column].apply(lambda value: np.nan if value == 'NaN ' else value)
    return data
