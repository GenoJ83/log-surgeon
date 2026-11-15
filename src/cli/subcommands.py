def handle_stats_command(entries):
    levels = {}
    for e in entries:
        levels[e.level] = levels.get(e.level, 0) + 1
    return levels
