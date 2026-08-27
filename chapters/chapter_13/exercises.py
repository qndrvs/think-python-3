## EXERCISES
import os, shelve, hashlib

# 1. Exercise 1
def replace_all(old: str, new: str, source_path: str, dest_path: str) -> None:
    reader = open(source_path, 'r', encoding = 'utf-8')
    content = reader.read()
    reader.close()

    new_content: str = content.replace(old, new)
    
    writer = open(dest_path, 'w', encoding='utf-8')
    writer.write(new_content)
    writer.close()

# 2. Exercise 2
def add_word(word: str, shelf: shelve.Shelf) -> None:
    key: str = ''.join(sorted(word.lower()))
    if key not in shelf: shelf[key] = [word]
    else:
        lst: list = shelf[key]
        lst.append(word)
        shelf[key] = lst

# 3. Exercise
def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest
def is_image(path: str, valid: list) -> bool:
    filename, ext = os.path.splitext(path)
    return ext.lower() in [e.lower() for e in valid]
extensions: list = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
db = shelve.open('photos/digests', 'n')

def add_path(path: str, shelf: shelve.Shelf):
    digest = md5_digest(path)
    if digest is None: return
    if digest not in shelf: shelf[digest] = [path]
    else:
        paths: list = shelf[digest]
        paths.append(path)
        shelf[digest] = paths
def walk_image(dirname: str):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            if is_image(path, extensions): add_path(path, db)
        elif os.path.isdir(path):
            walk_image(path)