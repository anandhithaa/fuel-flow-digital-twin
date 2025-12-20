def hourly_demand(hour):
    if 6 <= hour <= 10:
        return 1.3
    if 18 <= hour <= 22:
        return 1.4
    return 1.0
