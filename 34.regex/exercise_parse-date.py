import re

def parse_date(date):
    date_regex = re.compile(r'([0-3][0-9])[\/\.,](0[0-9]|1[0-2])[\/\.,]([12]\d{3})\b')
    match = date_regex.search(date)
    if match:
        d = match.group(1)
        m = match.group(2)
        y = match.group(3)
        return {'d':d, 'm':m, 'y':y}
    return None
