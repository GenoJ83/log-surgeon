from src.cli.parser import create_arg_parser

def test_cli_parser():
    p = create_arg_parser()
    args = p.parse_args(['syslog.log', '--level', 'ERROR'])
    assert args.file == 'syslog.log'
    assert args.level == 'ERROR'
