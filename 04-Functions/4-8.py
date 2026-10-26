def time_string(hours, minutes, time_format):
    if time_format == 12:
        if hours > 12:
            str_hours = str(hours - 12)
            hour_name = "PM"
            str_minutes = str(minutes)
            result = str_hours + ":" + str_minutes + hour_name
            return result
        else:
            str_hours = str(hours)
            hour_name = "AM"
            str_minutes = str(minutes)
            result = str_hours + ":" + str_minutes + hour_name
            return result
    elif time_format == 24:
        str_hours = str(hours)
        str_minutes = str(minutes)
        result = str_hours + ":" + str_minutes
        return result

time = time_string(14, 56, 12)
print(f'{time}')
