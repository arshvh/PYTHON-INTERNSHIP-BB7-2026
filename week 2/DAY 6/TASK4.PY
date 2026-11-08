import os

# Get the current Python file location
folder_path = os.path.dirname(os.path.abspath(__file__))

# Read input file
input_file = os.path.join(folder_path, "input.txt")

# Create output file
output_file = os.path.join(folder_path, "copy.txt")

with open(input_file, "r") as file:
    data = file.read()

with open(output_file, "w") as file:
    file.write(data)

print("File copied successfully!")