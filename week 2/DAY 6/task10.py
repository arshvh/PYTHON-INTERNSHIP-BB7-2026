from pathlib import Path

# Get current folder
current_folder = Path.cwd()

# Find notes.txt
file_path = current_folder / "notes.txt"

# Check if file exists
if file_path.exists():
    print("File Size:", file_path.stat().st_size, "bytes")
    print("File Extension:", file_path.suffix)
else:
    print("File not found!")