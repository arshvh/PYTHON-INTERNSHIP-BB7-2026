from pathlib import Path

# Give relative file path
relative_path = Path("data/raw_data.txt")

# Convert relative path to absolute path
absolute_path = relative_path.resolve()

# Print absolute path
print("Relative Path:", relative_path)
print("Absolute Path:", absolute_path)