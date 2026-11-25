import pytest
pytest.importorskip("pydantic")
from src.formatters.csv_formatter import format_csv
from src.models.entry import LogEntry

def test_csv_formatter():
    csv_text = format_csv([LogEntry(message='test')])
    assert 'test' in csv_text
