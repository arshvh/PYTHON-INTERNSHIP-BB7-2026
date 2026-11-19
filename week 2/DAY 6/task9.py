from pathlib import Path

# Get current folder
current_folder = Path.cwd()

# Define backup folder
backup_folder = current_folder / "backup"

# Check whether folder exists
if backup_folder.exists():
    print("Backup folder already exists.")
else:
    backup_folder.mkdir()
    print("Backup folder created successfully.")