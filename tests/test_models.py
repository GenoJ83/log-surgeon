from src.models.entry import LogEntry

def test_log_entry_defaults():
    e = LogEntry(message='Server reboot')
    assert e.level == 'INFO'
    assert e.message == 'Server reboot'
