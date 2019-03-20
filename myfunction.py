def minutes_seconds_to_hours(seconds, minutes=70):
    result = minutes / 60.0 + seconds / 3600
    return result

result = minutes_seconds_to_hours(300, 200) + 10
print(result)
