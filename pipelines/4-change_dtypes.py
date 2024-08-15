def change_dtypes(data):
    data['delivery_person_age'] = data['delivery_person_age'].astype(float)
    data['delivery_person_ratings'] = data['delivery_person_ratings'].astype(float)
    data['multiple_deliveries'] = data['multiple_deliveries'].astype(float)
    data['vehicle_condition'] = data['vehicle_condition'].astype(float)
    return data