def print_progress_bar(iteration, total, length=40):
    percent = f'{100 * (iteration / float(total)):.1f}'
    filled = int(length * iteration // total)
    bar = '=' * filled + '-' * (length - filled)
    print(f'\rProcessing: [{bar}] {percent}%', end='\r')
    if iteration == total:
        print()
