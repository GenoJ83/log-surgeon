import argparse

def create_arg_parser():
    p = argparse.ArgumentParser(prog='logsurgeon', description='High-performance log extraction CLI')
    p.add_argument('file', nargs='?', help='Log file to analyze')
    p.add_argument('--level', help='Filter by log level')
    p.add_argument('--keyword', help='Search for keyword')
    p.add_argument('--format', choices=['text', 'json', 'csv', 'html'], default='text')
    return p
