import re

def censor(pattern):
    censor_regex = re.compile(r'\b(frack[a-z]*)', re.I)
    censored_string = censor_regex.sub('CENSORED', pattern)
    return censored_string
    
