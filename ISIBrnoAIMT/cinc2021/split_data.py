import os
import random
import shutil

def split_data(source_dir, train_dir, test_dir, test_ratio=0.2, seed=42):
    """
    Split files from source_dir into training and testing sets.
    
    Args:
        source_dir (str): Directory containing all the files.
        train_dir (str): Directory to store training files.
        test_dir (str): Directory to store testing files.
        test_ratio (float): Proportion of files to reserve for testing.
        seed (int): Random seed for reproducibility.
    """
    # Create train and test directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Get all files in the source directory
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Shuffle files for randomness
    random.seed(seed)
    random.shuffle(all_files)

    # Calculate the number of test files
    test_size = int(len(all_files) * test_ratio)

    # Split files into test and train sets
    test_files = all_files[:test_size]
    train_files = all_files[test_size:]

    # Move files to their respective directories
    for file in test_files:
        shutil.move(os.path.join(source_dir, file), os.path.join(test_dir, file))
    for file in train_files:
        shutil.move(os.path.join(source_dir, file), os.path.join(train_dir, file))

    print(f"Moved {len(test_files)} files to {test_dir}")
    print(f"Moved {len(train_files)} files to {train_dir}")

if __name__ == "__main__":
    # Define source and target directories
    source_dir = r"/data/newc6477/AllDataPhysionet2021/"
    train_dir = r"/data/newc6477/physionet/train"
    test_dir = r"/data/newc6477/phyionet/test"

    # Split data
    split_data(source_dir, train_dir, test_dir, test_ratio=0.2)
