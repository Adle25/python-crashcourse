from pathlib import Path

file_path = Path('poem.txt')

try:
    constents = file_path.read_text()
except FileNotFoundError:
    print(f'File {file_path} do not exist!')
else:
    words = constents.lower().split()
    result = words.count('the')
    print(result)
    