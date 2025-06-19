import os
import shutil
import sys
import datetime

def backup_files(source_dir, destination_dir):
    """
    Copies all files from a source directory to a destination directory.
    If a file with the same name exists in the destination, a timestamp
    is appended to the filename to ensure uniqueness.

    Args:
        source_dir (str): The path to the source directory.
        destination_dir (str): The path to the destination directory.
    """
    print(f"Starting backup from '{source_dir}' to '{destination_dir}'...")

    # 1. Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # 2. Check if destination directory exists, create if not
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it...")
        try:
            os.makedirs(destination_dir)
            print("Destination directory created successfully.")
        except OSError as e:
            print(f"Error: Could not create destination directory '{destination_dir}': {e}")
            return
    elif not os.path.isdir(destination_dir):
        print(f"Error: Destination path '{destination_dir}' exists but is not a directory.")
        return

    # 3. Iterate over files in the source directory
    copied_count = 0
    skipped_count = 0
    error_count = 0

    try:
        for filename in os.listdir(source_dir):
            source_filepath = os.path.join(source_dir, filename)

            # Only process files, skip directories
            if os.path.isfile(source_filepath):
                destination_filepath = os.path.join(destination_dir, filename)

                # Check if the file already exists in the destination
                if os.path.exists(destination_filepath):
                    # Append timestamp to the filename
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    name_parts = os.path.splitext(filename)
                    new_filename = f"{name_parts[0]}_{timestamp}{name_parts[1]}"
                    destination_filepath = os.path.join(destination_dir, new_filename)
                    print(f"Conflict: '{filename}' already exists. Saving as '{new_filename}'")

                try:
                    shutil.copy2(source_filepath, destination_filepath) # copy2 preserves metadata
                    print(f"Copied: '{filename}' to '{destination_filepath}'")
                    copied_count += 1
                except Exception as e:
                    print(f"Error copying '{filename}': {e}")
                    error_count += 1
            else:
                print(f"Skipped: '{filename}' (not a file or is a directory).")
                skipped_count += 1

        print("\nBackup process completed.")
        print(f"Summary: Copied {copied_count} files, Skipped {skipped_count} items, Encountered {error_count} errors.")

    except OSError as e:
        print(f"Error during file processing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        print("Example: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)