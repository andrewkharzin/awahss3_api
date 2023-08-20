from datetime import datetime

def format_date_template(date_str):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # Define month abbreviations
    month_abbreviations = {
        1: 'JAN',
        2: 'FEB',
        3: 'MAR',
        4: 'APR',
        5: 'MAY',
        6: 'JUN',
        7: 'JUL',
        8: 'AUG',
        9: 'SEP',
        10: 'OCT',
        11: 'NOV',
        12: 'DEC',
    }

    # Extract day and month from the datetime object
    day = date_obj.day
    month = month_abbreviations[date_obj.month]

    # Format the date as "DDMON"
    formatted_date = f"{day:02d}{month}"
    return formatted_date
