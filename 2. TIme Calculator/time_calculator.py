def add_time(start, duration, day=None):
    time, period = start.split()  # time = '11:06', period = 'PM'
    initial_period = period

    hr_start, min_start = time.split(':')  # hr_start = '11', min_start = '06'
    hr_duration, min_duration = duration.split(':')  # hr_duration = '2', min_duration = '02'

    min_new = int(min_start) + int(min_duration)  # raw addition of hours
    hr_new = int(hr_start) + int(hr_duration)  # raw addition of minutes

    periods_later = 0
    days_later = 0

    DAYS_OF_WEEK = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    if min_new > 59:  # Converting extra minutes to hours
        min_new -= 60
        hr_new += 1

    hr_new_period = hr_new

    while hr_new > 12:  # keeping hr_new below 12 to know the hour within 12 hrs
        hr_new -= 12  # hr_new_period does not change

    while hr_new_period > 11:  # Checking to see if AM or PM has changed
        hr_new_period -= 12
        period = "PM" if period == "AM" else "AM"
        periods_later += 1

    if periods_later % 2 != 0:
        if initial_period == "PM":
            periods_later += 1
        else:
            periods_later -= 1

    days_later = periods_later / 2  # Calculating days from periods of 12 hrs

    new_time = f"{hr_new}:{str(min_new).zfill(2)} {period}"

    if day:
        day_index = DAYS_OF_WEEK.index(day.title())
        new_day_index = int((day_index + days_later) % 7)
        new_time += f", {DAYS_OF_WEEK[new_day_index]}"

    if days_later == 1:
        new_time += " (next day)"

    if days_later > 1:
        new_time += f" ({int(days_later)} days later)"

    return new_time
