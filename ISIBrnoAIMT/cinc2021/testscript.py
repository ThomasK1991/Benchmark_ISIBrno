from team_code import find_thresholds
from pathlib import Path
model_directory = r"C:\Users\Thomas Kaprielian\Documents\Master's Thesis\Benchmarking\ISIBrnoAIMT (1)\ISIBrnoAIMT\cinc2021\model"
filename = Path(model_directory, f'PROGRESS_{0}.pickle')

find_thresholds(filename,model_directory)