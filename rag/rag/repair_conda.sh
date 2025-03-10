#!/bin/bash

# Activate the base environment
eval "$(conda shell.bash hook)"
conda activate base

# Get the list of all channels except "defaults"
channels=$(conda config --show channels | grep -v "channels:" | grep -v "defaults" | sed 's/^- //')

# Loop through each channel and remove it
for channel in $channels; do
    conda config --remove channels "$channel"
done

# Ensure "defaults" is the only channel
conda config --add channels defaults

# Set the solver to libmamba
conda config --set solver libmamba

# Revert the base environment to revision 0
conda install --rev 0 -y

echo "Conda base environment has been reset successfully."
