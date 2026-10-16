from src.parsers.regex_parser import parse_line

def test_regex_parser():
    e = parse_line('[2026-11-15 10:00:00] ERROR: Disk full')
    assert e.level == 'ERROR'
    assert e.message == 'Disk full'
