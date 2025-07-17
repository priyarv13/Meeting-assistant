# deadline_parser.py
import dateparser

def convert_deadline_to_date(deadline_text):
    parsed_date = dateparser.parse(deadline_text, settings={'PREFER_DATES_FROM': 'future'})
    return parsed_date.strftime('%Y-%m-%d') if parsed_date else None
