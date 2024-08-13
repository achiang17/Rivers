#!/bin/bash

#SBATCH --job-name=usa_time_mse_adaDT5_logQ3.yml
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --gres=gpu:1 # :v100:1 or p100:1  
#SBATCH --time=24:00:00 # adjust as necessary
#SBATCH --mem-per-gpu=16GB # adjust as necessary
#SBATCH --mail-user=achiang@caltech.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

set -euo pipefail # kill the job if anything fails
set -x # echo script
nh-run train --config-file /groups/esm/achiang/Rivers/examples/catchment_models/neuralhydrology/usa_time_mse_adaDT5_logQ3.yml
echo done
