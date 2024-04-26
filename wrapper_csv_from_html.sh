#!/bin/bash

# Prompt the user for the path to the as_result_complete folder
read -p "Enter the path to the folder containing all antismash results: " folder_path

# Check if the folder exists
if [ ! -d "$folder_path" ]; then
  echo "Error: Folder not found."
  exit 1
fi

> ../all_regions.csv

echo "Directory Name, Region, Type, From, To, Most similar known cluster, miBiG Type, Similarity" >> ../all_regions.csv
# Iterate through each organims folder inside antismash results folder
for dir in "$folder_path"/*; do
  if [ -d "$dir" ]; then
    echo "Processing folder: $dir"
    # Navigate to the folder and run html_extraction.py
    cd "$dir" || exit
    python /home/gyanesh/Scripts/html_extraction.py
    sort regions_info.csv | uniq > temp 
    cat temp >> ../all_regions.csv
    rm regions_info.csv temp
    # Navigate back to the original directory
    cd - || exit
  fi
done

echo "Script execution complete."
