import re

def is_valid_time(time_string):
    # time_regex = re.compile(r'\b^\d{1,2}:\d{1,2}\b')
    # better regex:
    time_regex = re.compile(r'^\d{1,2}:\d\d$')
    match = time_regex.fullmatch(time_string)
    if match:
    	return True
    return False

print(is_valid_time('10:30'))
print(is_valid_time('10:300'))
