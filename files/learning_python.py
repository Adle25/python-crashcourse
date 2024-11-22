from pathlib import Path

path = Path('test.txt')
contents = path.read_text()

for line in contents.splitlines():
    if 'Python' in line:
        line = line.replace('Python', 'C')

    print(line)