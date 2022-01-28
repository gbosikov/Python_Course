def convert_time(duration: int) -> str:
    days = duration // 86400  # колличество дней
    hours = (duration - days * 86400) // 3600  # колличество часов
    minutes = (duration - days * 86400 - hours * 3600) // 60  # колличество минут
    seconds = duration - days * 86400 - hours * 3600 - minutes * 60  # колличество секунд
    return str(days) + ' days', str(hours) + ' hours', str(minutes) + ' minutes', str(seconds) + ' seconds'


duration = 500
result = convert_time(duration)
print(result)
