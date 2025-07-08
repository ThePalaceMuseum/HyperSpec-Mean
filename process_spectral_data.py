#!/usr/bin/env python3
"""
Spectral Data Processing Script

This script processes .txt files in the current directory:
- Skips the first 7 header lines
- Extracts columns 1 (wavelength) and 4 (mean values) from each data row
- Saves the extracted data as CSV files with the same filename but .csv extension

Usage:
1. Place this script in the directory containing your .txt spectral data files
2. Run: python process_spectral_data.py
"""

import os
import csv
import glob
from pathlib import Path


def process_txt_file(input_file_path, output_file_path):
    """
    Process a single .txt file and extract columns 1 and 4.
    
    Args:
        input_file_path (str): Path to the input .txt file
        output_file_path (str): Path to the output .csv file
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # Skip the first 7 header lines
        data_lines = lines[7:]
        
        # Extract columns 1 and 4 from each data line
        extracted_data = []
        
        for line_num, line in enumerate(data_lines, start=8):  # Start from line 8 for error reporting
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            # Split the line by whitespace (handles multiple spaces)
            columns = line.split()
            
            if len(columns) >= 4:  # Ensure we have at least 4 columns
                try:
                    wavelength = float(columns[0])  # Column 1
                    mean_value = float(columns[3])  # Column 4 (0-indexed, so index 3)
                    extracted_data.append([wavelength, mean_value])
                except ValueError as e:
                    print(f"Warning: Could not parse line {line_num} in {input_file_path}: {line.strip()}")
                    print(f"Error: {e}")
                    continue
            else:
                print(f"Warning: Line {line_num} in {input_file_path} has fewer than 4 columns: {line.strip()}")
        
        # Write the extracted data to CSV file
        with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(['Wavelength', 'Mean'])
            # Write data
            writer.writerows(extracted_data)
        
        print(f"Successfully processed: {input_file_path} -> {output_file_path}")
        print(f"  Extracted {len(extracted_data)} data rows")
        
    except Exception as e:
        print(f"Error processing {input_file_path}: {e}")


def main():
    """
    Main function to process all .txt files in the current directory.
    """
    # Get the current directory where the script is located
    current_directory = os.getcwd()

    # Find all .txt files in the current directory
    txt_files = glob.glob("*.txt")

    if not txt_files:
        print(f"No .txt files found in the current directory: {current_directory}")
        print("Please ensure this script is placed in a directory containing .txt spectral data files.")
        return

    print(f"Processing .txt files in: {current_directory}")
    print(f"Found {len(txt_files)} .txt files to process...")
    print("-" * 50)

    # Process each .txt file
    processed_count = 0
    for txt_file in txt_files:
        # Create output filename (same name but with .csv extension)
        base_name = os.path.splitext(txt_file)[0]
        output_file = f"{base_name}.csv"

        # Process the file
        process_txt_file(txt_file, output_file)
        processed_count += 1
        print()  # Add blank line for readability

    print("-" * 50)
    print(f"Processing complete! Successfully processed {processed_count} files.")
    print(f"CSV files have been saved in the current directory: {current_directory}")


if __name__ == "__main__":
    main()
