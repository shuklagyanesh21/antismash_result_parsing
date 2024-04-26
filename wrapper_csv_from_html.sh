#!/bin/bash

# Prompt the user for the path to the as_result_complete folder
read -p "Enter the path to the as_result_complete folder: " folder_path

# Check if the folder exists
if [ ! -d "$folder_path" ]; then
  echo "Error: Folder not found."
  exit 1
fi

# Iterate through each folder inside as_result_complete
for dir in "$folder_path"/*; do
  if [ -d "$dir" ]; then
    echo "Processing folder: $dir"
    # Navigate to the folder and run html_extraction.py
    cd "$dir" || exit
    python /home/gyanesh/Scripts/html_extraction.py
    regions_info.csv >> ../all_regions.csv
    # Navigate back to the original directory
    cd - || exit
  fi
done

echo "Script execution complete."

