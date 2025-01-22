import os
import shutil

# Define directories
source_directory = r"C:\Users\Thomas Kaprielian\Documents\4yp_Data\physionet.org\files\challenge-2021\1.0.3\training\ningbo\g8"  # Folder containing additional files
destination_directory = r"C:\Users\Thomas Kaprielian\Documents\Master's Thesis\Benchmarking\ISIBrnoAIMT (1)\ISIBrnoAIMT\cinc2021\test_data"  # Folder with existing data

target_classes = {'164889003','164890007','6374002','426627000','733534002',
               '713427006','270492004','713426002','39732003','445118002',
               '164947007','251146004','111975006','698252002','426783006',
               '284470004','10370003','365413008','427172004','164917005',
               '47665007','427393009','426177001','427084000','164934002',
               '59931005'}

# Function to extract classes from header files
def extract_classes_from_folder(folder):
    found_classes = set()
    for file_name in os.listdir(folder):
        if file_name.endswith(".hea"):  # Process only header files
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith("# Dx:"):
                        dx_classes = line.strip().replace("# Dx:", "").split(',')
                        found_classes.update(cls.strip() for cls in dx_classes)
    return found_classes

# Identify classes not present in the destination folder
found_classes = extract_classes_from_folder(destination_directory)
missing_classes = target_classes - found_classes

print(f"Classes found: {found_classes}")
print(f"Classes missing: {missing_classes}")

# Move files corresponding to missing classes
for file_name in os.listdir(source_directory):
    if file_name.endswith(".hea"):  # Process only header files
        source_path = os.path.join(source_directory, file_name)
        with open(source_path, 'r') as file:
            for line in file:
                if line.startswith("# Dx:"):
                    dx_classes = line.strip().replace("#Dx:", "").split(',')
                    file_classes = {cls.strip() for cls in dx_classes}
                    # Check if any missing class is in the file
                    if missing_classes & file_classes:
                        # Move associated files (.hea and .mat)
                        base_name = os.path.splitext(file_name)[0]
                        for ext in ['.hea', '.mat']:
                            src_file = os.path.join(source_directory, base_name + ext)
                            dest_file = os.path.join(destination_directory, base_name + ext)
                            if os.path.exists(src_file):
                                shutil.copy(src_file, dest_file)
                                print(f"Moved: {src_file} -> {dest_file}")
