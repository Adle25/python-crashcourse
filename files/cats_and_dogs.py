from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogs.txt')

try:
    cats_content = cats_path.read_text()
    dogs_content = dogs_path.read_text()
except FileNotFoundError:
    pass
else:
    print(cats_content)
    print()
    print(dogs_content)