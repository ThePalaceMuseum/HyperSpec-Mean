# ENVI Spectral Data Processor

A Python script for processing ENVI ASCII Plot Files (.txt) and extracting specific spectral data columns into CSV format for analysis and visualization.

## Description

This script automates the conversion of ENVI spectral data files by:
- Reading multiple .txt files from the current directory where the script is located
- Skipping header information (first 7 lines)
- Extracting wavelength (column 1) and mean values (column 4) from 6-column spectral data
- Saving the extracted data as CSV files with proper headers in the same directory

Perfect for researchers and analysts working with hyperspectral data from gemstones, minerals, or other materials analyzed using ENVI software. The script is portable and can be used in any directory containing ENVI spectral data files.

## Prerequisites

- **Python 3.6 or higher**
- **Standard Python libraries** (no additional packages required):
  - `os` - File system operations
  - `csv` - CSV file handling
  - `glob` - File pattern matching
  - `pathlib` - Path handling

## File Structure Requirements

### Input Folder Structure
```
your_workspace/
├── 1 天然翡翠.txt               # Sample spectral data file
├── 2 翡翠B货.txt                # Sample spectral data file
├── ...                         # Additional .txt files
└── process_spectral_data.py    # The processing script
```

**Note**: The script processes all .txt files in the same directory where it's located. No specific folder structure is required.

### Input File Format Specifications

Each .txt file must follow this exact structure:

**Lines 1-7: Header Information (skipped)**
```
ENVI ASCII Plot File [Mon Jul 07 14:50:29 2025]
Column 1: Wavelength
Column 2: Min: ROI #8~~2##255,0,0
Column 3: Mean-StdDev: ROI #8~~21##0,200,0
Column 4: Mean: ROI #8~~0##0,0,0
Column 5: Mean+StdDev: ROI #8~~21##0,200,0
Column 6: Max: ROI #8~~2##255,0,0
```

**Line 8 onwards: Data Rows (6 columns each)**
```
   399.360998  0.000000  0.056124  0.136450  0.216776  0.518519
   400.982707  0.000000  0.083957  0.158695  0.233433  0.432099
   402.604417  0.000000  0.092514  0.163083  0.233652  0.380435
   ...
```

## Installation Instructions

1. **Download the script**: Save `process_spectral_data.py` to the directory containing your .txt spectral data files

2. **Verify Python installation**:
   ```bash
   python --version
   ```
   Ensure you have Python 3.6 or higher installed.

3. **Prepare your data**:
   - Place the script in the same directory as your .txt spectral data files
   - No specific folder structure is required

4. **No additional dependencies**: The script uses only Python standard libraries.

## Usage Instructions

### Step-by-Step Guide

1. **Open terminal/command prompt** in the directory containing your .txt files and the script

2. **Run the script**:
   ```bash
   python process_spectral_data.py
   ```

3. **Monitor progress**: The script will display:
   - Current directory being processed
   - Number of files found
   - Processing status for each file
   - Number of data rows extracted per file
   - Final summary

4. **Check results**: CSV files will be created in the same directory as the .txt files

### Expected Output

```
Processing .txt files in: C:\Users\YourName\Desktop\spectral_data
Found 64 .txt files to process...
--------------------------------------------------
Successfully processed: 1 天然翡翠.txt -> 1 天然翡翠.csv
  Extracted 372 data rows

Successfully processed: 2 翡翠B货.txt -> 2 翡翠B货.csv
  Extracted 372 data rows

...

--------------------------------------------------
Processing complete! Successfully processed 64 files.
CSV files have been saved in the current directory: C:\Users\YourName\Desktop\spectral_data
```

## Input File Format Details

### Header Structure (Lines 1-7)
| Line | Content | Purpose |
|------|---------|---------|
| 1 | `ENVI ASCII Plot File [timestamp]` | File type identifier |
| 2 | `Column 1: Wavelength` | Column 1 description |
| 3 | `Column 2: Min: ROI #...` | Column 2 description |
| 4 | `Column 3: Mean-StdDev: ROI #...` | Column 3 description |
| 5 | `Column 4: Mean: ROI #...` | Column 4 description (extracted) |
| 6 | `Column 5: Mean+StdDev: ROI #...` | Column 5 description |
| 7 | `Column 6: Max: ROI #...` | Column 6 description |

### Data Structure (Line 8+)
- **Format**: 6 columns separated by spaces
- **Column 1**: Wavelength values (nm) - **EXTRACTED**
- **Column 2**: Minimum values
- **Column 3**: Mean minus standard deviation
- **Column 4**: Mean values - **EXTRACTED**
- **Column 5**: Mean plus standard deviation  
- **Column 6**: Maximum values

## Output Format

### CSV File Structure
```csv
Wavelength,Mean
399.360998,0.13645
400.982707,0.158695
402.604417,0.163083
404.226127,0.149646
405.847836,0.16018
...
```

### File Naming Convention
- **Input**: `original_filename.txt`
- **Output**: `original_filename.csv`
- **Location**: Same directory as input files and the script

## Example

### Sample Input File (`1 天然翡翠.txt`)
```
ENVI ASCII Plot File [Mon Jul 07 14:50:29 2025]
Column 1: Wavelength
Column 2: Min: ROI #8~~2##255,0,0
Column 3: Mean-StdDev: ROI #8~~21##0,200,0
Column 4: Mean: ROI #8~~0##0,0,0
Column 5: Mean+StdDev: ROI #8~~21##0,200,0
Column 6: Max: ROI #8~~2##255,0,0
   399.360998  0.000000  0.056124  0.136450  0.216776  0.518519
   400.982707  0.000000  0.083957  0.158695  0.233433  0.432099
   402.604417  0.000000  0.092514  0.163083  0.233652  0.380435
```

### Generated Output File (`1 天然翡翠.csv`)
```csv
Wavelength,Mean
399.360998,0.136450
400.982707,0.158695
402.604417,0.163083
```

## Error Handling

The script includes comprehensive error handling for:

### Common Issues and Solutions

| Issue | Error Message | Solution |
|-------|---------------|----------|
| No .txt files | `No .txt files found in the current directory` | Add .txt files to the directory or move script to correct location |
| Invalid data format | `Warning: Could not parse line X` | Check file format matches specifications |
| Insufficient columns | `Warning: Line X has fewer than 4 columns` | Verify data integrity |
| File access issues | `Error processing filename.txt: [details]` | Check file permissions |

### Data Validation
- **Empty lines**: Automatically skipped
- **Malformed data**: Logged with line numbers
- **Missing columns**: Reported but processing continues
- **Invalid numbers**: Conversion errors logged

## File Organization

### Before Processing

```
spectral_data_directory/
├── 1 天然翡翠.txt
├── 2 翡翠B货.txt
├── 3 翡翠B+C.txt
├── ...
└── process_spectral_data.py
```

### After Processing

```
spectral_data_directory/
├── 1 天然翡翠.txt
├── 1 天然翡翠.csv          # ← New CSV file
├── 2 翡翠B货.txt
├── 2 翡翠B货.csv           # ← New CSV file
├── 3 翡翠B+C.txt
├── 3 翡翠B+C.csv           # ← New CSV file
├── ...
└── process_spectral_data.py
```

## Troubleshooting

### Script Won't Run

1. **Check Python installation**: `python --version`
2. **Verify file location**: Ensure script is in the same directory as your .txt files
3. **Check file permissions**: Ensure you have read/write access to the directory

### No Files Processed

1. **Verify .txt files exist** in the same directory as the script
2. **Check file extensions**: Must be `.txt` (case-sensitive)
3. **Ensure files aren't empty** or corrupted

### Incomplete Data Extraction
1. **Check file format**: Verify 7-line header structure
2. **Validate data columns**: Ensure 6 columns per data row
3. **Review error messages**: Check console output for specific issues

### Performance Issues
- **Large files**: Processing time increases with file size
- **Many files**: Progress is reported for each file
- **Memory usage**: Script processes files one at a time

## Support

For issues or questions:
1. Check the error messages in the console output
2. Verify your input files match the expected format
3. Ensure all prerequisites are met
4. Review the troubleshooting section above

---

**Script Version**: 1.0  
**Compatible with**: Python 3.6+  
**Last Updated**: July 2025
