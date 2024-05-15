# JPEG recovery

**This is not reccommended for serious usage!**

This project is result of one laboratory of computer security course.

## Description

The metadata of the FAT file system was damaged, and both FAT tables were deleted. Therefore, the task involves scanning data clusters for JPEG file structures and reconstructing the images.

## Implementation

The script, written in Python, scans an input binary file for JPEG headers (`{0XFF, 0XD8, 0XFF, 0XE0, 0X00, 0X10, 0X4A, 0X46, 0X49, 0X46}`) and extracts data until the end of the JPEG file (`{0xFF, 0xD9, 0x00, 0x00}`) is detected. Extracted images are saved as `output-%d.jpg`.

## How to Use

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/forensic-analysis.git
    cd forensic-analysis
    ```

2. Run the script:
    ```sh
    python jpeg_recovery.py inputfile.bin
    ```
   Replace `inputfile.bin` with the path to your binary input file.