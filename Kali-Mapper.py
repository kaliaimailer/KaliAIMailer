import os

def create_map(dir_path, stats=None):
    """Recursively creates a map of the directory structure, counting files, directories, and file types."""
    if stats is None:
        stats = {'files': 0, 'dirs': 0, 'file_types': {}}
    
    items = os.listdir(dir_path)
    for item in items:
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            stats['dirs'] += 1
            create_map(item_path, stats)
        else:
            stats['files'] += 1
            _, ext = os.path.splitext(item)
            if ext in stats['file_types']:
                stats['file_types'][ext] += 1
            else:
                stats['file_types'][ext] = 1
    return stats

def save_map_to_file(stats, file_path='directory_map.txt'):
    """Saves the directory map statistics to a file."""
    with open(file_path, 'w') as f:
        f.write(f"Total directories: {stats['dirs']}\n")
        f.write(f"Total files: {stats['files']}\n")
        f.write("File types and counts:\n")
        for ext, count in stats['file_types'].items():
            f.write(f"{ext if ext else 'No extension'}: {count}\n")

root_dir = '.'  # Start directory

# Generate the directory map and collect stats
stats = create_map(root_dir)

# Save the stats to directory_map.txt
save_map_to_file(stats)

print("Directory map and statistics have been saved to directory_map.txt.")
