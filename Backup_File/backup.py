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