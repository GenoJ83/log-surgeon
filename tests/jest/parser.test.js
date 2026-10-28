const { parseLogLine, countSeverities } = require('../../js/parser');

describe('LogSurgeon JavaScript Parser', () => {
  it('correctly parses structured bracketed timestamp log lines', () => {
    const line = '[2026-11-16 12:00:00] ERROR: Out of memory in worker process';
    const parsed = parseLogLine(line);
    expect(parsed.level).toBe('ERROR');
    expect(parsed.timestamp).toBe('2026-11-16 12:00:00');
    expect(parsed.message).toContain('Out of memory');
  });

  it('handles unstructured text with default INFO level', () => {
    const line = 'Simple standard console output';
    const parsed = parseLogLine(line);
    expect(parsed.level).toBe('INFO');
    expect(parsed.message).toBe('Simple standard console output');
    expect(parsed.timestamp).toBeNull();
  });

  it('aggregates severity counts accurately', () => {
    const logs = [
      { level: 'ERROR' },
      { level: 'ERROR' },
      { level: 'WARNING' },
      { level: 'INFO' }
    ];
    const counts = countSeverities(logs);
    expect(counts.ERROR).toBe(2);
    expect(counts.WARNING).toBe(1);
    expect(counts.INFO).toBe(1);
  });

  it('gracefully handles empty and null inputs', () => {
    expect(parseLogLine(null).message).toBe('');
    expect(parseLogLine('').message).toBe('');
  });
});
