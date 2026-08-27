## EXTENSIONS
import os, hashlib, shelve, datetime

# 1. Extension 1 - File system as a data source
"""
a. Write a function called file_inventory(directory) that walks a directory recursively using os.walk and returns a list of tuples:
    (absolute_path, filename, extension, size_bytes)
   Use os.path.getsize, os.path.splitext, os.path.join. Skip hidden files (those starting with '.'). Add a docstring with parameter and return type documentation.
b. Write a function called group_by_extension(inventory) that takes the output of file_inventory and returns a dictionary mapping each extension (lowercase, e.g. '.py', '.txt', '.csv') to a list of (path, size) tuples. Extensions should be normalized to lowercase.
c. Write a function called extension_summary(inventory) that prints:
   === File Inventory Summary ===
   Extension   Count   Total Size (KB)   Avg Size (KB)
   .py         12      48.3              4.0
   .txt        5       120.1             24.0
   ...
   Sorted by total size descending. Format sizes to 1 decimal place.
d. Write a function called find_large_files(inventory, threshold_kb) that returns a list of (path, size_kb) tuples for files larger than threshold_kb, sorted by size descending.
"""
print("\nEXTENSION 1")

# 1.a
def file_inventory(directory: str) -> list:
    """
    Recursively walk a directory and collect basic metadata for every non-hidden file found.

    Parameters
    ----------
    directory : str
        Path of the directory to scan (scanned recursively, including all subdirectories).

    Returns
    -------
    list
        A list of tuples, one per non-hidden file found. Hidden files (names starting with '.') are skipped.
        [(absolute_path, filename, extension, size_bytes)]

    Examples
    --------
    >>> file_inventory('photos')
    [('photos/img001.jpg', 'img001', '.jpg', 204800), ('photos/notes.txt', 'notes', '.txt', 512)]
    >>> file_inventory('empty_dir')
    []
    >>> file_inventory('docs')
    [('docs/reports/q1.pdf', 'q1', '.pdf', 102400)]
    """
    result: list = []
    for main, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('.'): continue
            absolute_path: str = os.path.join(main, file)
            filename, extension = os.path.splitext(file)
            size_bytes: int = os.path.getsize(absolute_path)
            result.append((absolute_path, filename, extension, size_bytes))
    return result

# 1.b
def group_by_extension(inventory: list) -> dict:
    result: dict = {}
    for abs_path, name, ext, size in inventory:
        ext = ext.lower()
        if ext not in result: result[ext] = [(abs_path, size)]
        else: result[ext].append((abs_path, size))
    return result

# 1.c
def extension_summary(inventory: list) -> None:
    result: dict = {}
    for abs_path, name, ext, size in inventory:
        ext = ext.lower()
        if ext not in result:
            result[ext] = {'count': 0, 'total_bytes': 0}
        result[ext]['count'] += 1
        result[ext]['total_bytes'] += size
    ordered: list = sorted(result.items(), key = lambda x: x[1]['total_bytes'], reverse = True)
    print(
        "=== File Inventory Summary ===\n"
        f"{'Extension':<12} {'Count':<7} {'Total Size (KB)':<18} {'Avg Size (KB)'}\n"
        "-" * 50
    )
    for ext, stats in ordered:
        count = stats['count']
        total_kb = stats['total_bytes'] / 1024.0
        avg_kb = total_kb / count if count > 0 else 0.0
        ext_display = ext if ext else "(no ext)"
        print(f"{ext_display:<12} {count:<7} {total_kb:<18.1f} {avg_kb:.1f}")

# 1.d
def find_large_files(inventory: list, threshold_kb: int) -> list:
    threshold_bytes: int = threshold_kb * 1024
    result: list = []

    for path, filename, ext, size in inventory:
        if size > threshold_bytes:
            size_kb = size / 1024.0
            result.append((path, size_kb))

    result.sort(key = lambda x: x[1], reverse = True)
    return result


# 2. Extension 2 - Content-based duplicate detection
"""
1. Write a function called file_hash(filepath) that computes the MD5 hash of a file's contents and returns it as a hex string. Use:
    import hashlib
    with open(filepath, 'rb') as f:
    return hashlib.md5(f.read()).hexdigest()
   The 'rb' mode reads in binary — necessary for non-text files.
   Add error handling: if the file cannot be read, return None.
2. Write a function called find_duplicates(directory) that:
   - Walks the directory with file_inventory
   - Computes the hash of each file
   - Returns a dictionary mapping each hash to a list of paths
   - Only includes hashes with more than one path (actual duplicates)
3. Write a function called duplicate_report(directory) that prints:
   === Duplicate Files Found ===
   Group 1 (hash: a3f2...):
   /path/to/file1.txt (2.3 KB)
   /path/to/copy/file1.txt (2.3 KB)
   Wasted space: 2.3 KB
   ...
   Total wasted space: X.X KB
   If no duplicates are found, print a confirmation message.
"""
print("\nEXTENSION 2")

# 2.a
def file_hash(filepath: str) -> str | None:
    try:
        with open(filepath, 'rb') as f:
            data: bytes = f.read()
            return hashlib.md5(data).hexdigest()
    except OSError:
        return None

# 2.b
def find_duplicates(directory: str) -> dict:
    inventory: list = file_inventory(directory)
    result: dict = {}

    for path, filename, ext, size in inventory:
        digest = file_hash(path)
        if digest is None: continue

        if digest not in result: result[digest] = [path]
        else: result[digest].append(path)

    return {fhash: paths for fhash, paths in result.items() if len(paths) > 1}

# 2.c
def duplicate_report(directory: str) -> None:
    duplicates: dict = find_duplicates(directory)

    if not duplicates:
        print("No duplicate files found.")
        return

    print("=== Duplicate Files Found ===")
    total_kb: float = 0.0
    group: int = 1

    for fhash, paths in sorted(duplicates.items(), key = lambda x: x[0]):
        print(f"\nGroup {group} (hash: {fhash[:8]}...):")
        info: list = []

        for path in paths:
            size_bytes = os.path.getsize(path)
            size_kb = size_bytes / 1024.0
            info.append((path, size_kb))
        if not info: continue

        info.sort(key = lambda x: x[0])
        for path, size_kb in info:
            print(f"  {path} ({size_kb:.1f} KB)")

        group_wasted_kb: float = info[0][1] * (len(info) - 1)
        total_kb += group_wasted_kb
        print(f"  Wasted space: {group_wasted_kb:.1f} KB")
        group += 1
        
    print(f"\nTotal wasted space: {total_kb:.1f} KB")


# 3. Extension 3 - Persistent data with shelve
"""
1. Write a function called open_vocab_db(filepath) that opens a shelve database and returns it. The database stores words as keys and dicts as values:
    {'definition': str, 'example': str, 'date_added': str, 'review_count': int}
2. Write a function called add_word(db, word, definition, example) that adds a new entry. Use import datetime; datetime.date.today().isoformat() for the date. If the word already exists, print a warning and do NOT overwrite.
3. Write a function called review_word(db, word) that increments review_count for the given word and prints its definition and example. If the word does not exist, print an error.
4. Write a function called words_to_review(db, min_reviews=0, max_reviews=3) that returns a list of words whose review_count is between min_reviews and max_reviews (inclusive). These are words that need more practice.
"""
print("\nEXTENSION 3")

# 3.a
def open_vocab_db(filepath: str) -> shelve.Shelf:
    return shelve.open(filepath, writeback = True)

# 3.b
def add_word(db: shelve.Shelf, word: str, definition: str, example: str) -> None:
    if word in db:
        print(f"Warning: The word '{word}' already exists in the database. Not overwriting.")
        return
    date: str = datetime.date.today().isoformat()
    db[word] = {
        'definition': definition,
        'example': example,
        'date_added': date,
        'review_count': 0
    }
    print(f"Successfully added '{word}' to the vocabulary.")

# 3.c
def review_word(db: shelve.Shelf, word: str) -> None:
    if word not in db:
        print(f"Error: The word '{word}' does not exist in the database.")
        return
    info: dict = db[word]
    info['review_count'] += 1
    print(f"======= Reviewing: {word} =======")
    print(f"Definition:   {info['definition']}")
    print(f"Example:      {info['example']}")
    print(f"Review Count: {info['review_count']}")

# 3.d
def words_to_review(db: shelve.Shelf, min_reviews: int = 0, max_reviews: int = 3) -> list:
    result: list = []
    for word, info in db.items():
        count: int = info.get('review_count', 0)
        if min_reviews <= count <= max_reviews: result.append(word)
    return result