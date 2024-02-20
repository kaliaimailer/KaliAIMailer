import os

def create_map(dir_path, stats={'files': 0, 'dirs': 0, 'py_files': 0, 'txt_files': 0}):
    """Recursively creates a map of the directory structure, counting files, directories, and specific file types."""
    items = os.listdir(dir_path)
    for item in items:
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            # It's a directory, increment directory count
            stats['dirs'] += 1
            # Recursively map the contents of the directory
            create_map(item_path, stats)
        else:
            # Increment total file count
            stats['files'] += 1
            # Check for specific file extensions and increment their counts
            if item.endswith('.py'):
                stats['py_files'] += 1
            elif item.endswith('.txt'):
                stats['txt_files'] += 1
    return stats

root_dir = '.'  # Start directory

# Initialize counts
stats = {'files': 0, 'dirs': 0, 'py_files': 0, 'txt_files': 0}

# Generate the directory map and collect stats
stats = create_map(root_dir, stats)

# Print the total counts
print(f"Total directories: {stats['dirs']}")
print(f"Total files: {stats['files']}")
print(f"Total .py files: {stats['py_files']}")
print(f"Total .txt files: {stats['txt_files']}")
