def remove_condition_from_weathercondition(data):
    data['weatherconditions'] = data['weatherconditions'].apply(lambda value: value.split(' ')[-1])
    return data