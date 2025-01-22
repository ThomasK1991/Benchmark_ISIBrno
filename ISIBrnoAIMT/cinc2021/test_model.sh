#!/bin/bash
#SBATCH --time=10:00:00
#SBATCH --job-name=train_model
#SBATCH --output=/users/newc6477/Benchmark_ISIBrno/Output/%j.out
#SBATCH --gres=gpu:1

echo "post sbatch commands"

# Credit to Jong Kwon & John McGonigle
abort() { >&2 printf '█%.0s' {1..40}; (>&2 printf "\n[ERROR] $(basename $0) has exited early\n"); exit 1; }  # print error message
scriptdirpath=$(cd -P -- "$(dirname -- "$0")" && pwd -P);
IFS=$'\n\t'; set -eo pipefail; # exits if error, and set IFS, so no whitespace error

trap 'abort' 0; set -u;
# Sets abort trap defined in line 2, set -u exits when detects unset variables

# cd into the scriptdirpath so that relative paths work
pushd "${scriptdirpath}" > /dev/null

# _________ ACTUAL CODE THAT RUNS STUFF __________

echo -e "ml cuda: \n"
ml cuda

CONDA_ENV="one_ext"

# Activate conda env if in base env, or don't if already set.
source "$(dirname $(dirname $(which conda)))/etc/profile.d/conda.sh"
if [[ "${CONDA_DEFAULT_ENV}" != "${CONDA_ENV}" ]]; then
  echo "activating ${CONDA_ENV} env"
  set +u; conda activate "${CONDA_ENV}"; set -u
fi

# Perform checks if debug is true
DEBUG=false
# Check if the debug argument is provided
if [[ $# -gt 0 && $1 == "--debug" ]]; then
    DEBUG=true
fi

if [ "$DEBUG" == true ]; then
  # Check python being used
  echo -e "______DEBUG MODE______\n"
  echo -e "python check: \n"
  which python
  
  echo -e "gpu(s) check: \n"
  nvidia-smi

  echo -e "Python, torch, and gpu(s) check \n\n"
  python ~/code/template_scripts/torch/testGPU.py

  echo -e "Checks complete\n"
fi

# Define paths
PYTHON_SCRIPT="/users/newc6477/Benchmark_ISIBrno/ISIBrnoAIMT/cinc2021/test_model.py"
MODEL_PATH="/users/newc6477/Benchmark_ISIBrno/ISIBrnoAIMT/cinc2021/model"
DATA_PATH="/data/newc6477/Test_data/test_data"
OUTPUT_PATH="/users/newc6477/Benchmark_ISIBrno/ISIBrnoAIMT/cinc2021/outputs"

# Run your Python script with all required arguments
python "$PYTHON_SCRIPT" "$MODEL_PATH" "$DATA_PATH" "$OUTPUT_PATH"

conda deactivate

# ___________ MORE SAFE CRASH JARGON ____________

popd > /dev/null

trap : 0
(>&2 echo "✔")
exit 0
