def get_hours_since_midnight (seconds):

    if seconds < 0 or seconds > 86400:
        return 0

    else:
        hours_since_midnight = seconds // 3600

    # Type the code to calculate total hours given n(number) of seconds
    # For example, given 3800 seconds the total hours is 1

        return hours_since_midnight

def get_minutes(seconds):

    if seconds < 0 or seconds > 86400 :
        return 0
    else:

        minutes = seconds // 60
        minutes_since_midnight = minutes % 60

    # Type the code to calculate total minutes less whole hour given n(number) of seconds
    # For example, given 3800 seconds the total minutes is 3

        return minutes_since_midnight

def get_seconds(seconds):

    if seconds < 0 or seconds > 86400:
        return 0
    else:

        seconds_since_midnight = seconds % 60

    # Type the code to calculate total minutes less whole hour given n(number) of seconds
    # For example, given 3800 seconds the total minutes is 20

        return seconds_since_midnight
