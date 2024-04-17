def dir_print(dirs):
    dirs.sort()
    for directory in dirs:
        depth = directory.count('/')
        print('  ' * (depth) + directory.split('/')[-1])

n = int(input())
dirs = [input() for _ in range(n)]
dir_print(dirs)