# Backup Script Documentation

## Overview
The `backup.py` Python script is designed to create backups of files from a specified source directory to a destination directory. It is invoked via the command line, taking two arguments: the source directory and the destination directory. The script ensures that files are copied with unique names by appending a timestamp to filenames if duplicates are found in the destination directory. It includes robust error handling to manage issues like missing directories or file copy failures.

## Features
- Copies all files (not directories) from the source directory to the destination directory.
- Checks for existing files in the destination directory and appends a timestamp to the filename to ensure uniqueness.
- Creates the destination directory if it does not exist.
- Provides clear error messages for invalid inputs or issues during execution.
- Handles exceptions gracefully to prevent crashes.

## Requirements
- **Python**: Version 3.x
- **Standard Libraries**: The script uses `os`, `sys`, `shutil`, and `datetime`, which are included with Python.
- No external libraries are required.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Save the script as `backup.py` in a directory of your choice.
3. No additional dependencies are needed, as the script uses Python's standard libraries.

## Code
```python
import os
import sys
import shutil
from datetime import datetime

def create_backup(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            sys.exit(1)
        
        # Check if destination directory exists, create if it doesn't
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"Created destination directory '{dest_dir}'.")
        
        # Get list of files in source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            
            # Skip if it's a directory
            if os.path.isdir(source_path):
                continue
                
            # Get destination file path
            dest_path = os.path.join(dest_dir, filename)
            
            # Check if file already exists in destination
            if os.path.exists(dest_path):
                # Generate timestamp for unique filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_filename)
                print(f"File '{filename}' already exists, saving as '{new_filename}'.")
            
            # Copy the file
            try:
                shutil.copy2(source_path, dest_path)
                print(f"Copied '{filename}' to '{dest_path}'.")
            except Exception as e:
                print(f"Error copying '{filename}': {e}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)
    
    # Get source and destination directories from command-line arguments
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    print(f"Starting backup from '{source_dir}' to '{dest_dir}'...")
    create_backup(source_dir, dest_dir)
    print("Backup completed.")
```

## How It Works
1. **Command-Line Arguments**:
   - The script expects two arguments: the source directory path and the destination directory path.
   - Example command: `python backup.py /path/to/source /path/to/destination`
   - If the wrong number of arguments is provided, it displays usage instructions and exits.

2. **Directory Validation**:
   - Checks if the source directory exists. If not, it prints an error and exits.
   - Checks if the destination directory exists. If not, it creates it using `os.makedirs()`.

3. **File Processing**:
   - Lists all items in the source directory using `os.listdir()`.
   - Skips directories, processing only files.
   - For each file, constructs the destination path.
   - If a file with the same name exists in the destination directory, appends a timestamp (format: `YYYYMMDD_HHMMSS`) to the filename to ensure uniqueness (e.g., `file.txt` becomes `file_20250810_230405.txt`).

4. **File Copying**:
   - Uses `shutil.copy2()` to copy files, preserving metadata (e.g., timestamps, permissions).
   - Prints a confirmation for each copied file or a modified filename if a timestamp was added.

5. **Error Handling**:
   - Catches and reports errors for invalid directories, file copy failures, or other issues.
   - Exits with a status code of 1 if critical errors occur (e.g., source directory missing).
   - Continues processing remaining files if a single file copy fails.

## Usage
1. Save the script as `backup.py`.
2. Open a terminal or command prompt and navigate to the directory containing `backup.py`.
3. Run the script with the source and destination directories as arguments:
   ```bash
   python backup.py /path/to/source /path/to/destination
   ```
4. The script will:
   - Create the destination directory if it doesn't exist.
   - Copy files from the source to the destination.
   - Append timestamps to filenames if duplicates are found.
   - Display progress messages and errors, if any.

## Example Output
```
Starting backup from '/path/to/source' to '/path/to/destination'...
Created destination directory '/path/to/destination'.
Copied 'document.txt' to '/path/to/destination/document.txt'.
File 'notes.txt' already exists, saving as 'notes_20250810_230405.txt'.
Copied 'notes.txt' to '/path/to/destination/notes_20250810_230405.txt'.
Error copying 'image.jpg': Permission denied
Backup completed.
```

## Error Handling
- **Invalid Arguments**: If the script is run with fewer or more than two arguments, it prints usage instructions and exits.
- **Non-existent Source Directory**: Exits with an error message if the source directory does not exist.
- **File Copy Errors**: Reports errors for individual files (e.g., permission issues) and continues processing other files.
- **General Exceptions**: Catches unexpected errors, prints them, and exits with a status code of 1.

## Notes
- The script uses `shutil.copy2()` to preserve file metadata, ensuring backups are as close as possible to the originals.
- The timestamp format (`%Y%m%d_%H%M%S`) ensures uniqueness and readability (e.g., `20250810_230405` for August 10, 2025, 11:04:05 PM).
- The script skips directories in the source folder; it only copies files.
- Adjust the script to handle subdirectories if needed by adding recursive copying with `shutil.copytree()`.

## Limitations
- Does not copy subdirectories or their contents.
- Does not provide options to overwrite existing files (always appends a timestamp).
- Does not support filtering files by type or other criteria.
- No logging to a file; output is printed to the console.

## Future Improvements
- Add support for recursive copying of subdirectories.
- Allow options to overwrite files or skip duplicates instead of renaming.
- Add file type filters (e.g., only copy `.txt` files).
- Implement logging to a file for backup history.
- Add command-line options for customizing the timestamp format or backup behavior.

## License
This script is provided as-is for educational and practical use. No warranty is implied. Use at your own risk.