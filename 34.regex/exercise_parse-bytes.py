import re

def parse_bytes(pattern):
    bytes_regex = re.compile(r'\b[01]{8}\b')
    return bytes_regex.findall(pattern)
