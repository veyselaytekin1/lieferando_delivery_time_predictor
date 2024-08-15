def transform_data(data):
    data['time_taken(min)'] = data['time_taken(min)'].apply(lambda value: float(value[-2:]))
    data['time_orderd'] = data['order_date'] + ' ' + data['time_orderd']
    data['time_order_picked'] = data['order_date'] + ' ' + data['time_order_picked']
    data['time_orderd'] = pd.to_datetime(data['time_orderd'], format = '%d-%m-%Y %H:%M:%S')
    data['time_order_picked'] = pd.to_datetime(data['time_order_picked'], format = '%d-%m-%Y %H:%M:%S')
    data['time_to_pick'] = (data['time_order_picked'] - data['time_orderd']) / np.timedelta64(1, 'm')
    monhts = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday',5:'Saturday', 6:'Sunday'}
    data['order_year'] = data['time_orderd'].apply(lambda value: value.year)
    data['order_month'] = data['time_orderd'].apply(lambda value: value.month).map(monhts)
    data['order_day'] = data['time_orderd'].apply(lambda value: value.dayofweek).map(days)
    return data