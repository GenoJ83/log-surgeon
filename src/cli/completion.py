ZSH_COMPLETION = '_logsurgeon() { _arguments "1: :_files" "--level:level:(DEBUG INFO WARNING ERROR CRITICAL)" "--format:format:(text json csv html)" }'

def print_zsh_completion():
    print(ZSH_COMPLETION)
