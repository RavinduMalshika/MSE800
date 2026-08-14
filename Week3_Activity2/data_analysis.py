file_path = "Week3_Activity2/junk.txt"

# Read existing lines and count them
with open(file_path, "r") as file:
    lines = file.readlines()
    print(f"Number of lines in file: {len(lines)}")

# Append a new line of text
with open(file_path, "a") as file:
    file.write("text file analysis\n")

# Read updated lines from the file
with open(file_path, "r") as file:
    updated_lines = file.readlines()

# Append the lowercase versions of all lines back to the file
with open(file_path, "w") as file:
    for line in updated_lines:
        file.write(line.lower())
