# YouTube Video Downloader

This is a simple Python script for downloading YouTube videos using the `yt-dlp` library.

## Requirements

- Python 3.x
- `yt-dlp` library

## Installation
1. Clone the repository
2. Navigate to your project directory: 
```bash
   cd path/to/your/project```
3. Create a virtual environment (optional):
```bash
   python3 -m venv venv```
4. Activate the virtual environment:
- On MacOs or Linux:
```bash
   source venv/bin/activate```
- On Windows:
```bash
   venv\Scripts\activate```
5. Install ```py-dlp```:
```bash
   pip install yt-dlp```
6. Run the script:
```bash
   python nameofthescript.py```
- Enter the YouTube video URL when prompted and wait for the download to complete.

## Features
- Downloads the highest resolution available for the given YouTube video URL.
- Simple and easy-to-use interface.
- Handles exceptions gracefully and provides meaningful error messages.