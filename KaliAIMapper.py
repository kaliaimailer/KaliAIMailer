import os

def create_directory_map(dir_path, output_file, prefix=''):
    """
    Recursively creates a map of the directory structure, listing all directories and files,
    and saves it to a file.
    
    Args:
    - dir_path: The path of the directory to map.
    - output_file: An open file object for writing the directory map.
    - prefix: A string prefix used for indentation to represent directory depth.
    """
    items = os.listdir(dir_path)
    for item in sorted(items):  # Sort items for consistent order
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            # Write the directory name
            output_file.write(f"{prefix}{item}/\n")
            # Recursively map the contents of the directory, with increased indentation
            create_directory_map(item_path, output_file, prefix + '    ')
        else:
            # Write the file name
            output_file.write(f"{prefix}{item}\n")

def save_directory_map(root_dir, map_file_path):
    """
    Generates a directory map starting from root_dir and saves it to map_file_path.
    
    Args:
    - root_dir: The root directory to start the mapping from.
    - map_file_path: The path to the file where the directory map will be saved.
    """
    with open(map_file_path, 'w') as output_file:
        create_directory_map(root_dir, output_file)

root_dir = '.'  # Start directory
map_file_path = 'kali_map.txt'

# Generate the directory map and save it to directory_map.txt
save_directory_map(root_dir, map_file_path)

print(f"Directory map has been saved to {map_file_path}.")
