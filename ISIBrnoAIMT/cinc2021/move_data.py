import os
import shutil

def collect_files(source_directory, target_directory, extensions=(".hea", ".mat")):
    """
    Traverse through the folder structure and copy all files with specified extensions
    to the target directory.

    Args:
        source_directory (str): The root directory to start searching.
        target_directory (str): The destination directory for the collected files.
        extensions (tuple): File extensions to collect (default: .hea, .mat).
    """
    # Create target directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)

    # Walk through the source directory
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.endswith(extensions):
                # Full path to the source file
                source_file = os.path.join(root, file)
                # Full path to the destination file
                target_file = os.path.join(target_directory, file)

                # Avoid overwriting files with the same name
                if os.path.exists(target_file):
                    print(f"File {file} already exists in target directory. Skipping...")
                    continue

                # Copy the file to the target directory
                shutil.copy(source_file, target_directory)
                print(f"Copied: {source_file} -> {target_directory}")

if __name__ == "__main__":
    # Specify the source directory containing the folders
    source_dir = "/data/newc6477/training/physionet.org/files/challenge-2021/1.0.3/training/"

    # Specify the target directory to store the collected files
    target_dir = "/data/newc6477/AllDataPhysionet2021/"

    # Collect .hea and .mat files
    collect_files(source_dir, target_dir)
