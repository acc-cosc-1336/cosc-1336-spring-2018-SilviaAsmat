def get_time(hour, minutes, seconds, time_type, meridian='AM'):
    '''
    Returns a time in 12 or 24 hour format

    :param hour: The hour of day-
                 when time_type 12 hr hour valid range 1 to 12 otherwise return 'Invalid hours(1-12)'
                 when time_type 24 hr hour valid range 0 to 23 otherwise return 'Invalid hours(range 0-23)'

    :param minutes: Minutes of an hour--minutes valid range 0 to 59 otherwise return 'Invalid minutes(range 0-59)'
    :param seconds:  seconds of an hour--seconds valid range 0 to 59 otherwise 'Invalid seconds(range 0-59)'
    :param time_type: Indicates the format of time to derive 12hr or 24hr
                      Valid time_type values 12 or 24 otherwise return 'Invalid time_type(12 or 24 only)'
                      If time_type is 24 ignore meridian value;

                      If time_type is 12hr time use meridian parameter value(AM or PM)

    :param meridian:  AM, PM

    :return: time in 12 or 24 hour format
      Example for 12 hour format 09:09:09 PM
      Example for 24 hour format 21:09:09
    ADD YOUR CODE AFTER THE THREE QUOTES BELOW (dont forget to include a return statement at the end
    '''
    if time_type == 12:
        if hour <1 or hour >12:
            return "Invalid hours(range 1-12)"
        if meridian != "AM" and meridian != "PM":
            return "Invalid meridian"

    elif time_type == 24:
        if hour <0 or hour >23:
            return "Invalid hours(range 0-23)"
    else:
        return "Invalid time_type(12 or 24 only)"

    if minutes <0 or minutes >59:
        return "Invalid minutes(range 0-59)"

    if seconds <0 or seconds >59:
        return "Invalid seconds(range 0-59)"

    # At this point, we have valid inputs
    time = ''
    #write decision structure code here
    hours_formatted = ''
    minutes_formatted = ''
    seconds_formatted = ''
    meridian_formatted = ''

    if hour <10 and hour >=0:
        # Hours is a single digit
        hours_formatted = '0' + str(hour)
    else:
        hours_formatted = str(hour)

    if minutes <10 and minutes>=0:
        # Minutes is a single digit
        minutes_formatted = '0' + str(minutes)
    else:
        minutes_formatted = str(minutes)

    if seconds<10 and seconds>=0:
        # Seconds is a single digit
        seconds_formatted = '0' + str(seconds)
    else:
        seconds_formatted = str(seconds)

    if time_type == 12:
        meridian_formatted = str(meridian)

    if time_type == 12:
        time = hours_formatted + ':' + minutes_formatted + ':' + seconds_formatted +' '+ meridian_formatted

    if time_type == 24:
       
        time = hours_formatted + ':' + minutes_formatted + ':' + seconds_formatted

    return time



def time_from_utc(utc_offset, utc_zero_time):
    '''
    Write code to calculate a time zone's time after applying utc_offset
    :param utc_offset:
    :param utc_zero_time:
    :return:
    DON NOT CHANGE ANYTHING IN THIS FUNCTION
    '''

    return (utc_zero_time + utc_offset) % 24

