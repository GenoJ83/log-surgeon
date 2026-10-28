/**
 * Node.js Log Line Parser & Severity Classifier
 */
function parseLogLine(line) {
  if (!line || typeof line !== 'string') {
    return { level: 'INFO', message: '', timestamp: null };
  }
  const match = line.match(/^\[([^\]]+)\]\s+(\w+):\s+(.*)$/);
  if (match) {
    return {
      timestamp: match[1],
      level: match[2].toUpperCase(),
      message: match[3]
    };
  }
  return { level: 'INFO', message: line.trim(), timestamp: null };
}

function countSeverities(logs) {
  const counts = { INFO: 0, WARNING: 0, ERROR: 0, DEBUG: 0 };
  for (const log of logs) {
    const lvl = (log.level || 'INFO').toUpperCase();
    counts[lvl] = (counts[lvl] || 0) + 1;
  }
  return counts;
}

module.exports = { parseLogLine, countSeverities };
